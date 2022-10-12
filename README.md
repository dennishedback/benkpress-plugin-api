# benkpress-plugin-api

Small plugin API to simplify the use of sklearn pipelines whose
training data have been built with the help of
[benkpress](https://github.com/dennishedback/benkpress),
without having to pull in all of benkpress as a dependency.
benkpress-plugin-api also uses a more permissive (BSD 2-clause) license
than benkpress proper does (GPLv3).

## API Reference

Since the API is small, the full API reference is included below.

Module benkpress_plugins
========================

Sub-modules
-----------
* benkpress_plugins.pipelines
* benkpress_plugins.preprocessors
  
Module benkpress_plugins.pipelines
==================================

Functions
---------

    
`DummyPipeline()`
:   Returns a dummy classifier pipeline to use as a baseline.

Module benkpress_plugins.preprocessors
======================================

Classes
-------

`PassthroughPreprocessor()`
:   Describes a generic page preprocessor which accepts all pages and passes through
the input as output. Can be used for page classification for trivial cases when there
is no need to transform the text.

    ### Methods

    `accepts_page(self, pagetext: str) ‑> bool`
    :

    `transform(self, pagetext: str) ‑> List[str]`
    :

`Preprocessor(*args, **kwargs)`
:   Describes a preprocessor which transforms PDF page text into data which can be 
    used in an sklearn compatible pipeline.

    ### Ancestors (in MRO)

    * typing.Protocol
    * typing.Generic

    ### Methods

    `accepts_page(self, pagetext: str) ‑> bool`
    :   Determines whether this PDF page should be transformed or not.
        
        Parameters
        ----------
        pagetext : The text of the current PDF page being processed.
        
        Returns
        -------
        Whether this page should be transformed or not.

    `transform(self, pagetext: str) ‑> List[str]`
    :   Transforms the text of PDF page into a format which can be used as training
        data by the classification pipeline.
        
        Parameters
        ----------
        pagetext : The text of the current PDF page being processed.
        
        Returns
        -------
        A list of strings each corresponding to a datapoint in the training data.
