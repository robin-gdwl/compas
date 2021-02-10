import bpy
import bpy.addon_utils as addon_utils


"""
A way to annotate vertices and edges in blender
uses the MeasureIt plugin
TODO: not sure if programmatically enabling a plugin in Blender is a good idea in general...
    It should work since the MeasureIt-Addon comes bundled with Blender and is rather robust.
"""

# _preferences = _bpy.context.preferences

__all__ = [
    'annotate_vertex',
]


def _enable_annotation_addon():
    """Enables the MeasureIt addon
    See here for documentation: https://docs.blender.org/manual/en/2.91/addons/3d_view/measureit.html

    Returns
    -------
    True if loading the addon was successfull, otherwise False

    """

    if addon_utils.enable("MeasureIt"):
        isloaded = True
    else: 
        isloaded = False

    return isloaded


def _disable_annotation_addon():
    """Disables the MeasureIt addon
    See here for documentation: https://docs.blender.org/manual/en/2.91/addons/3d_view/measureit.html
    
    Returns
    -------
    True if the addon is still loaded, otherwise False

    """

    if addon_utils.disable("MeasureIt"):
        isloaded = True
    else:
        isloaded = False

    return isloaded


def annotate_vertex(vertex, label, color=None, size=1):
    """Labels a specified vertex with a string or Number.
    
    Parameters
    ----------
    vertex : Mesh vertex
        A mesh vertex
    label : str
    color : tuple, optional
    size : double, optional

    Examples
    -------
    .. code-block:: python

        import addon_utils
        import bpy
        print("    "*300)
        result = addon_utils.enable("measureit")
        print(result)
        #result = addon_utils.disable("measureit")
        print(result)
        a_mesh = bpy.data.objects["Cube"]
        print(type(a_mesh))
        print(a_mesh.items())
        print(a_mesh.data)

    """
    pass


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':
    pass
