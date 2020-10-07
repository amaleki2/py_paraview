from utils import *
file_name = 'stl_example.stl'

# read and plot a stl mesh. rendering option can take many values. Some different values are shown below
# if interact=True, visualization window is activated.
read_mesh_file(file_name, rendering_option="Surface", interact=True)

# clip the stl mesh with a plane. plane is spciefied by origin and normal vectors.
# opa indicate the opacity of the cutted area
plot_clip(file_name,  origin=[0.4, 0.5, 0.5], normal=[0.7, -0.6, 0.2], opa=0.2, rendering_option='Surface', interact=True)

# plot a vtk mesh. Meshes are visualized using the rendering_option parameter
file_name = 'vtk_example.vtk'
read_mesh_file(file_name, rendering_option="Surface With Edges", interact=True)

# in addition to vtk, two additional similar formats are vtu (xml unstructed) and vts (xml structured) which typically
# contain field values (like pressure or velocity) over the mesh file.
# plot vtu file with different options. the file contain pressure and x-velocity and y-velocity information.
file_name = 'vtu_example.vtu'
read_mesh_file(file_name, rendering_option="Points", interact=True)
read_mesh_file(file_name, rendering_option="Surface", interact=True, colored_by=('POINTS', 'Pressure'))
read_mesh_file(file_name, rendering_option="Surface", interact=True, colored_by=('POINTS', 'Velocity', 'X'))

# plot levelsets of pressure at 0.97, 0.99 and 1.01
plot_isosurfaces(file_name, levelsets=[0.97, 0.99, 1.01], source=['POINTS', 'Pressure'], rendering_option='Surface', interact=True)

# plot pressure, x velocity and y velocity over a line connecting two points (0, -8.0) , (0. 8.0)
plot_over_line(file_name, ['Pressure', 'Velocity_X', 'Velocity_Y'], [0.0, -8.0, 0.0], [0.0, 8.0, 0.0], interact=True)

# plot vts mesh that contains temperature and pressure values.
file_name = 'vts_example.vts'
read_mesh_file(file_name, rendering_option="Surface", interact=True)
read_mesh_file(file_name, rendering_option="Surface", interact=True, colored_by=('CELLS', 'pressure'))
plot_isosurfaces(file_name, rendering_option='Surface', interact=True)

# plot an obj file.
file_name = 'obj_example.obj'
read_mesh_file(file_name, rendering_option="Surface With Edges", interact=True)


