import os
import bpy

__all__ = [
    'get_document_basename',
    'get_document_filename',
    'get_document_extension',
    'get_document_filepath',
    'get_document_dirname'
]


def get_document_basename():
    """Get the name of the Blender document (including the extension).

    Returns
    -------
    str or None
        The name of the document or None if the document is still "Untitled".
    """
    filepath = get_document_filepath()
    return os.path.basename(filepath)


def get_document_filename():
    """Get the name of the Blender document without the file extension.

    Returns
    -------
    str or None
        The name of the document or None if the document is still "Untitled".
    """
    basename = get_document_basename()
    if not basename:
        return None
    return os.path.splitext(basename)[0]


def get_document_extension():
    """Get the extension of the Blender document (including the dot separator).

    Returns
    -------
    str or None
        The extension of the document or None if the document is still "Untitled".
    """
    basename = get_document_basename()
    if not basename:
        return None
    return os.path.splitext(basename)[1]


def get_document_filepath():
    """Get the full path to the Blender document.

    Returns
    -------
    str or None
        The path to the document or None if the document is still "Untitled".
    """
    return bpy.data.filepath


def get_document_dirname():
    """Get the name of the directory containing the Blender document.

    Returns
    -------
    str or None
        The name of the directory or None if the document is still "Untitled".
    """
    filepath = get_document_filepath()
    if not filepath:
        return None
    return os.path.dirname(filepath)


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    pass
