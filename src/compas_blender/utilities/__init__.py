"""
********************************************************************************
utilities
********************************************************************************

.. currentmodule:: compas_blender.utilities

This package contains low-level functions for working and interacting with Blender.


collections
============
Functions to manage Blender `collections <https://docs.blender.org/manual/en/latest/scene_layout/collections/collections.html>`_.

.. autosummary::
    :toctree: generated/

    create_collection
    create_collections
    create_collections_from_path
    clear_collection
    clear_collections


data
=====

.. autosummary::
    :toctree: generated/

    delete_unused_data

document
=========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    get_document_basename
    get_document_filename
    get_document_extension
    get_document_filepath
    get_document_dirname


drawing
========

.. autosummary::
    :toctree: generated/

    draw_points
    draw_pointcloud
    draw_lines
    draw_cylinders
    draw_spheres
    draw_cubes
    draw_mesh
    draw_faces
    draw_texts


objects
=======

.. autosummary::
    :toctree: generated/

    delete_object
    delete_objects
    delete_object_by_name
    delete_objects_by_names
    get_object_by_name
    get_objects_by_names

misc
=======

.. autosummary::
    :toctree: generated/

    unload_modules

annotating
==========

.. autosummary::
    :toctree: generated/

    annotate_vertex

"""

from .data import *  # noqa: F401 F403
from .document import *  # noqa: F401 F403
from .objects import *  # noqa: F401 F403
from .collections import *  # noqa: F401 F403
from .drawing import *  # noqa: F401 F403
from .misc import *  # noqa: F401 F403
# from .annotating import *  # noqa: F401 F403


__all__ = [name for name in dir() if not name.startswith('_')]
