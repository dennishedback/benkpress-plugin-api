#! /usr/bin/env python3

# Copyright (c) 2022, Dennis Hedback
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from dataclasses import dataclass
from importlib.metadata import entry_points, EntryPoint
from typing import List, Dict, Protocol

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.dummy import DummyClassifier


class PagePreprocessor(Protocol):
    """
    Describes the preprocessor stage of a PDFClassiferContext.
    """

    def transform(self, pagetext: str) -> List[str]:
        """
        Transforms the text of PDF page into a format which can be used as training
        data by the classification pipeline.

        Parameters
        ----------
        pagetext : The text of the current PDF page being processed.

        Returns
        -------
        A list of strings each corresponding to a datapoint in the training data.

        """

    def accepts_page(self, pagetext: str) -> bool:
        """
        Determines whether this PDF page should be transformed or not.

        Parameters
        ----------
        pagetext : The text of the current PDF page being processed.

        Returns
        -------
        Whether this page should be transformed or not.
        """


class PassthroughPagePreprocessor:
    """
    Describes a generic page preprocessor which accepts all pages and passes through
    the input as output. Can be used for page classification for trivial cases when there
    is no need to transform the text.
    """

    def transform(self, pagetext: str) -> List[str]:
        return [pagetext]

    def accepts_page(self, pagetext: str) -> bool:
        return True



@dataclass
class PDFClassifierContext:
    """
    Describes a context in which a PDF classifier can operate. The preprocessor does
    any preprocessing needed for the page data to be used in an sklearn compatible
    pipeline. The pipeline parameter is the aforementioned sklearn compatible pipeline.
    """

    preprocessor: PagePreprocessor
    pipeline: Pipeline

_PREPROCESSORS: Dict[str, EntryPoint] = {}
_PIPELINES: Dict[str, EntryPoint] = {}


def get_available_preprocessors() -> List[str]:
    """
    Get the names of all installed preprocessors.

    Returns
    -------
    List containing the names of all available preprocessor plugins.
    """
    return [x for x in _PREPROCESSORS]


def get_available_pipelines() -> List[str]:
    """
    Get the names of all installed pipelines.

    Returns
    -------
    List containing the names of all available pipeline plugins.
    """
    return [x for x in _PIPELINES]


def get_preprocessor_entry_point(name: str) -> EntryPoint:
    """
    Get preprocessor entry point.

    Parameters
    ----------
    name : The name of the installed preprocessor.

    Returns
    -------
    EntryPoint used to load the preprocessor plugin.
    """
    return _PREPROCESSORS[name]


def get_pipeline_entry_point(name: str) -> EntryPoint:
    """
    Get pipeline entry point.

    Parameters
    ----------
    name : The name of the installed pipeline.

    Returns
    -------
    EntryPoint used to load the pipeline plugin.
    """
    return _PIPELINES[name]
