from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()


def read_mesh_file(file_name, rendering_option='Surface', create_new_view=True, colored_by=None, interact=False):
    # rendering_choice = 'Surface'
    # rendering_choice = 'Points'
    if file_name[-3:] == "vtk":
        mesh = LegacyVTKReader(FileNames=[file_name])
    elif file_name[-3:] == "obj":
        mesh = WavefrontOBJReader(FileName=file_name)
    elif file_name[-3:] == "stl":
        mesh = STLReader(FileNames=[file_name])
    elif file_name[-3:] == "vts":
        mesh = XMLStructuredGridReader(FileName=file_name)
    elif file_name[-3:] == "vtu":
        mesh = XMLUnstructuredGridReader(FileName=file_name)
    else:
        raise (NotImplemented("%s files are not supported" % (file_name[-3:])))

    view = CreateView("RenderView") if create_new_view else GetActiveView()

    display = Show(mesh, view, 'UnstructuredGridRepresentation')
    display.SetRepresentationType(rendering_option)

    if colored_by:
        ColorBy(display, colored_by)

    if interact:
        Interact()
    return mesh, view, display


def plot_isosurfaces(file_name, levelsets=None, source=None, rendering_option='Surface', interact=False, colored_by=None):
    mesh, view, display = read_mesh_file(file_name, rendering_option=rendering_option, interact=False, colored_by=colored_by)

    try:
        contour1 = Contour(Input=mesh)
    except AttributeError:
        raise (IOError("contour cannot not defined for this mesh file."))

    if levelsets: contour1.Isosurfaces = levelsets
    if source: contour1.ContourBy = source #['POINTS', 'Pressure']
    contour_display = Show(contour1, view, 'UnstructuredGridRepresentation')
    contour_display.Representation = rendering_option
    Hide(mesh, view)

    if interact: Interact()


def plot_clip(file_name, origin, normal, opa=0.5, rendering_option='Surface', interact=False, colored_by=None):
    mesh, view, display = read_mesh_file(file_name, interact=False, rendering_option=rendering_option)

    try:
        clip = Clip(Input=mesh)
    except AttributeError:
        raise (IOError("contour cannot not defined for this mesh file."))

    clip_display = Show(clip, view, 'UnstructuredGridRepresentation')
    clip_display.Representation = rendering_option
    Hide(mesh, view)

    clip.ClipType.Origin = origin
    clip.ClipType.Normal = normal

    display = Show(mesh, view, 'UnstructuredGridRepresentation')

    display.Opacity = opa
    if colored_by:
        ColorBy(display, colored_by)

    if interact:
        Interact()


def plot_over_line(file_name, plot_parameters, x1, x2, interact=False, rendering_option='Surface'):
    mesh, view, display = read_mesh_file(file_name, interact=False, rendering_option=rendering_option)
    layout = GetLayout()
    line = PlotOverLine(Input=mesh, Source='High Resolution Line Source')
    line.Source.Point1 = x1 #[-8.0, -8.0, 0.0]
    line.Source.Point2 = x2 #[32.0, 8.0, 0.0]
    line_display = Show(line, view, 'UnstructuredGridRepresentation')
    line_display.Representation = rendering_option

    line_chart_view = CreateView('XYChartView')
    line_display_1 = Show(line, line_chart_view, 'XYChartRepresentation')
    line_display_1.SeriesVisibility = plot_parameters #['Pressure', 'Velocity_X', 'Velocity_Y']
    AssignViewToLayout(view=line_chart_view, layout=layout, hint=0)

    if interact: Interact()