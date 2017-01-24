

sphinxcontrib-srclinks
========================
| Source: https://github.com/westurner/sphinxcontrib-srclinks
| Source: https://github.com/westurner/sphinxcontrib-srclinks/blob/develop/sphinxcontrib/srclinks/__init__.py
| Source: https://github.com/westurner/sphinxcontrib-srclinks/blob/develop/sphinxcontrib/srclinks/_templates/srclinks.html

A sphinx extension to add links to various views of the documentation page source in the sphinx jinja2 template sidebar.

Features
-----------

* Specify ``srclink_project`` in sphinx conf.py
* Add links to {Source, Edit, History, Annotate} and {GitHub, BitBucket,} URLs to the Sphinx HTML template sidebar.
* Add links to {https://./user/repo/, and e.g. https://./tree/[srclink_branchname]}

* (Sphinx HTML Documentation Sidebar)

    * This Page
    
      * Source RST
      * Source
      * Edit
      * History
      * Annotate
      
    * `github.com/westurner/sphinxcontrib-srclinks <https://github.com/westurner/sphinxcontrib-srclinks>`_ / 
      `master <https://github.com/westurner/sphinxcontrib-srclinks/tree/master>`_
    
      * git clone https://github.com/westurner/sphinxcontrib-srclinks
      * git clone git@github.com/westurner/sphinxcontrib-srclinks
      * git clone ssh://git@github.com/westurner/sphinxcontrib-srclinks

Usage
-------

- Clone the sphinxcontrib-srclinks repo

.. code:: bash

    git clone https://github.com/westurner/sphinxcontrib-srclinks
    
- Copy ``srclinks.html`` to the ``_templates/srclinks.html`` folder:

.. code:: bash

    DOCS="./docs/"
    mkdir -p "$DOCS/_templates"
    cp sphinxcontrib-srclinks/sphinxcontrib/srclinks/_templates/srclinks.html \
        "$DOCS/_templates/srclinks.html"

- BLD: conf.py: Configure the ``srclink_`` settings in conf.py (``test_html_page_context()``)

.. code:: python

    # conf.py
    srclink_project = 'https://github.com/westurner/sphinxcontrib-srclinks'
    srclink_project = 'https://bitbucket.org/westurner/sphinxcontrib-srclinks'
    srclink_project = 'hg@bitbucket.org/westurner/sphinxcontrib-srclinks'
    srclink_project = 'git@bitbucket.org/westurner/sphinxcontrib-srclinks'
    srclink_src_path = 'docs/'
    srclink_branch = 'master'

    
- BLD: conf.py: Add ``srclinks.html`` to ``html_sidebars`` in ``conf.py``:

.. code:: Python

    # Custom sidebar templates, maps document names to template names.
    html_sidebars = {
        '**': [
            'localtoc.html',
            'relations.html',
            'searchbox.html',
            'srclinks.html',
            ],
        'index': [
            'globaltoc.html',
            'relations.html',
            'searchbox.html',
            'srclinks.html',
            ],
    }
    

License
===========
BSD 3-Clause
