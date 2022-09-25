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

from abc import abstractmethod
from typing import List
from dataclasses import dataclass
from sklearn.pipeline import Pipeline

class PagePreprocessor:
    """
    Describes the preprocessor stage of a PDFClassiferContext.
    """

    @abstractmethod
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

    @abstractmethod
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


@dataclass
class PDFClassifierContext:
    """
    Describes a context in which a PDF classifier can operate. The preprocessor does
    any preprocessing needed for the page data to be used in an sklearn compatible
    pipeline. The pipeline parameter is the aforementioned sklearn compatible pipeline.
    """

    preprocessor: PagePreprocessor
    pipeline: Pipeline


