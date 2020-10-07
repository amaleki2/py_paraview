# py_paraview
This repo contains examples for how paraview can be used in an external python environment for visualizing 2D and 3D objects. 

The examples show how different mesh file formats including `vtk`, `vts`, `vtu`, `obj` and `stl` can be read with paraview python API.
In addition, operations like clipping onto a plane, plotting onto a line or plotting levelsets are demonstrated. 

## paraview python installation
In order to install paraview library, follow the below instructions. 

- Install paraview: download paraview from `https://www.paraview.org/download/` and run to install.  
- Add he following folders to your PATH variable   
    `$PARAVIEW/bin/`, `$PARAVIEW/bin/Lib/`, `$PARAVIEW/bin/Lib/site-packages`. $PARAVIEW` is the installation folder of paraview. 
    For example, in windows, itshould be found at C:\Program Files\Paraview. 

- Create a conda environment : 

   `conda create paraview python=$PARAVIEW_PYTHON_VERSION`, 
   
   where `$PARAVIEW_PYTHON_VERSION` is the python version used for paraview installation. 
   To check what version of python paraview is installed with, run `pvpython.exe` in `$PARAVIEW/bin/` 

- Add paraview to your pythonpath:  
  find the installation folder of your conda environment `ENV_INSTALATION_FOLDER`. In windows, this can be found at 
  `C:\Users\$MYNAME\Anaconda\envs\paraview`. 
  Add `pv1.pth` and `pvt2.pth` files in the `$ENV_INSTALATION_FOLDER/Lib/site-packages`:

```
#pv1.pth
pv1.pth which contains 
import sys; os.path.join(os.path, "$PARAVIEW\bin\Lib\site-packages"); 
```
and
```
#pv2.pth
pv2.pth which contains  
$PARAVIEW\bin\Lib\site-packages 
```
- test:
  Open a python shell in your conda environement and run the following code to test. 
```  
from paraview.simple import * 
sphere = Sphere(ThetaResolution=16, PhiResolution=32) 
shrink = Shrink(sphere) 
Show(shrink) 
Interact() 
```


Note: You may see some errors like

`#osp: INITIALIZATION ERROR --> could not open module lib ospray_module_ispc: The specified module could not be found.`

The program still works. This error has created some conversation 
[here](https://discourse.paraview.org/t/could-not-open-module-lib-ospray-module-ispc/4079) 
and [here](https://gitlab.kitware.com/paraview/paraview-superbuild/-/merge_requests/766).