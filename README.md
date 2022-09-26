# benkpress-api

Small API to simplify the use of sklearn pipelines whose
training data have been built with the help of
[benkpress](https://github.com/dennishedback/benkpress),
without having to pull in all of benkpress as a dependency.
benkpress-api also uses a more permissive (BSD 2-clause) license
than benkpress proper does (GPLv3).

## API Reference

Since the API is small, the full API reference is included below.

### Classes

`PDFClassifierContext(preprocessor: benkpress_api.PagePreprocessor, pipeline: sklearn.pipeline.Pipeline)`
:   Describes a context in which a PDF classifier can operate. The preprocessor does
any preprocessing needed for the page data to be used in an sklearn compatible
pipeline. The pipeline parameter is the aforementioned sklearn compatible pipeline.

    ### Class variables

    `pipeline: sklearn.pipeline.Pipeline`
    :

    `preprocessor: benkpress_api.PagePreprocessor`
    :

`PagePreprocessor()`
:   Describes the preprocessor stage of a PDFClassiferContext.

    ### Descendants

    * benkpress_api.PassthroughPagePreprocessor

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

`PassthroughPagePreprocessor()`
:   Describes a generic page preprocessor which accepts all pages and passes through
the input as output. Can be used for page classification for trivial cases without
any need to

    ### Ancestors (in MRO)

    * benkpress_api.PagePreprocessor
