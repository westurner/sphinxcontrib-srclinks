

sphinxcontrib-srclinks
========================
Add links to {Source, Edit, History, Annotate} with {GitHub, BitBucket,} to the Sphinx HTML template sidebar.

* Source: https://github.com/westurner/sphinxcontrib-srclinks
* Source: https://github.com/westurner/sphinxcontrib-srclinks/blob/develop/sphinxcontrib/srclinks/__init__.py
  srclinks.py contexts
* Source: https://github.com/westurner/sphinxcontrib-srclinks/blob/develop/sphinxcontrib/srclinks/_templates/srclinks.html : srclinks.html template


Usage
-------
Clone the repo and copy ``srclinks.html`` into the docs' ``_templates/``
folder:

.. code:: bash

    git clone https://bitbucket.org/westurner/sphinxcontrib-srclinks

    DOCS="path/to/docs"
    mkdir -p $DOCS/_templates
    cp sphinxcontrib-srclinks/sphinxcontrib/srclinks/_templates/srclinks.html \
        $DOCS/_templates/srclinks.html

Configure the ``srclink_`` settings for the desired repo in ``conf.py``:

.. code:: python

    # conf.py| Source: | Source: 
    srclink_project = 'https://github.com/westurner/sphinxcontrib-srclinks'
    srclink_project = 'https://bitbucket.org/westurner/sphinxcontrib-srclinks'
    srclink_project = 'hg@bitbucket.org/westurner/sphinxcontrib-srclinks'
    srclink_project = 'git@bitbucket.org/westurner/sphinxcontrib-srclinks'
    srclink_src_path = 'docs/'
    srclink_branch = 'master'
    
Add ``srclinks.html`` to ``html_sidebars`` in ``conf.py``:

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
    

