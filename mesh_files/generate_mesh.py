from pyevtk.hl import gridToVTK, pointsToVTK, unstructuredGridToVTK
import numpy as np
import random as rnd

nx, ny, nz = 6, 6, 4
lx, ly, lz = 1.0, 1.0, 1.0
dx, dy, dz = lx/nx, ly/ny, lz/nz
ncells = nx * ny * nz
npoints = (nx + 1) * (ny + 1) * (nz + 1)

X = np.arange(0, lx + 0.1*dx, dx, dtype='float64')
Y = np.arange(0, ly + 0.1*dy, dy, dtype='float64')
Z = np.arange(0, lz + 0.1*dz, dz, dtype='float64')
x = np.zeros((nx + 1, ny + 1, nz + 1))
y = np.zeros((nx + 1, ny + 1, nz + 1))
z = np.zeros((nx + 1, ny + 1, nz + 1))

for k in range(nz + 1):
    for j in range(ny + 1):
        for i in range(nx + 1):
            x[i, j, k] = X[i] + (0.5 - rnd.random()) * 0.2 * dx
            y[i, j, k] = Y[j] + (0.5 - rnd.random()) * 0.2 * dy
            z[i, j, k] = Z[k] + (0.5 - rnd.random()) * 0.2 * dz

pressure = np.random.rand(ncells).reshape((nx, ny, nz))
temp = np.random.rand(npoints).reshape((nx + 1, ny + 1, nz + 1))

#generate vts
gridToVTK("./structured", x, y, z, cellData={"pressure": pressure}, pointData={"temp": temp})

# generate vtu, this is only the points, no mesh
pointsToVTK("./unstructured", x, y, z, data=None)

#generate vtu with temperature data saved at points, no mesh
pointsToVTK("./unstructured", x, y, z, data={"temp": temp})

# if you want to generate vtu with mesh, you need to specify two additional parameters of the mesh.
# connectivity: 1D array that defines the vertices associated to each element.
#                   Together with offset define the connectivity or topology of the grid.
#                   It is assumed that vertices in an element are listed consecutively.
#     offsets: 1D array with the index of the last vertex of each element in the connectivity array.
#              It should have length nelem, where nelem is the number of cells or elements in the grid.
# unstructuredGridToVTK("./unstructured", x, y, z, connectivity=some_vector, offsets=some_vector,
#                       cellData={"pressure": pressure}, pointData={"temp": temp})