"""
This type stub file was initially generated by pyright
"""
from typing import Iterable

loss_name = ...
model_name = ...
EOS = ...
BOW = ...
EOW = ...
displayed_errors = ...

def eprint(*args, **kwargs):  # -> None:
    ...

class _Meter:
    def __init__(self, fasttext_model, meter) -> None: ...
    def score_vs_true(self, label):  # -> tuple[NDArray[Unknown], NDArray[Any]]:
        """Return scores and the gold of each sample for a specific label"""
        ...
    def precision_recall_curve(
        self, label=...
    ):  # -> tuple[NDArray[Unknown], NDArray[Any]]:
        """Return precision/recall curve"""
        ...
    def precision_at_recall(self, recall, label=...):
        """Return precision for a given recall"""
        ...
    def recall_at_precision(self, precision, label=...):
        """Return recall for a given precision"""
        ...

class _FastText:
    """
    This class defines the API to inspect models and should not be used to
    create objects. It will be returned by functions such as load_model or
    train.

    In general this API assumes to be given only unicode for Python2 and the
    Python3 equvalent called str for any string-like arguments. All unicode
    strings are then encoded as UTF-8 and fed to the fastText C++ API.
    """

    def __init__(self, model_path=..., args=...) -> None: ...
    def set_args(self, args=...):  # -> None:
        ...
    def is_quantized(self): ...
    def get_dimension(self):
        """Get the dimension (size) of a lookup vector (hidden layer)."""
        ...
    def get_word_vector(self, word):  # -> NDArray[Unknown]:
        """Get the vector representation of word."""
        ...
    def get_sentence_vector(self, text):  # -> NDArray[Unknown]:
        """
        Given a string, get a single vector represenation. This function
        assumes to be given a single line of text. We split words on
        whitespace (space, newline, tab, vertical tab) and the control
        characters carriage return, formfeed and the null character.
        """
        ...
    def get_nearest_neighbors(self, word, k=..., on_unicode_error=...): ...
    def get_analogies(self, wordA, wordB, wordC, k=..., on_unicode_error=...): ...
    def get_word_id(self, word):
        """
        Given a word, get the word id within the dictionary.
        Returns -1 if word is not in the dictionary.
        """
        ...
    def get_label_id(self, label):
        """
        Given a label, get the label id within the dictionary.
        Returns -1 if label is not in the dictionary.
        """
        ...
    def get_subword_id(self, subword):
        """
        Given a subword, return the index (within input matrix) it hashes to.
        """
        ...
    def get_subwords(
        self, word, on_unicode_error=...
    ):  # -> tuple[Unknown, NDArray[Unknown]]:
        """
        Given a word, get the subwords and their indicies.
        """
        ...
    def get_input_vector(self, ind):  # -> NDArray[Unknown]:
        """
        Given an index, get the corresponding vector of the Input Matrix.
        """
        ...
    def predict(
        self,
        text: str,
        k: int = ...,
        threshold: float = ...,
        on_unicode_error: str = ...,
    ) -> Iterable[
        tuple[str, float]
    ]:  # -> tuple[Unknown, Unknown] | tuple[Any | tuple[()], NDArray[Unknown]]:
        """
        Given a string, get a list of labels and a list of
        corresponding probabilities. k controls the number
        of returned labels. A choice of 5, will return the 5
        most probable labels. By default this returns only
        the most likely label and probability. threshold filters
        the returned labels by a threshold on probability. A
        choice of 0.5 will return labels with at least 0.5
        probability. k and threshold will be applied together to
        determine the returned labels.

        This function assumes to be given
        a single line of text. We split words on whitespace (space,
        newline, tab, vertical tab) and the control characters carriage
        return, formfeed and the null character.

        If the model is not supervised, this function will throw a ValueError.

        If given a list of strings, it will return a list of results as usually
        received for a single line of text.
        """
        ...
    def get_input_matrix(self):  # -> NDArray[Unknown]:
        """
        Get a reference to the full input matrix of a Model. This only
        works if the model is not quantized.
        """
        ...
    def get_output_matrix(self):  # -> NDArray[Unknown]:
        """
        Get a reference to the full output matrix of a Model. This only
        works if the model is not quantized.
        """
        ...
    def get_words(
        self, include_freq=..., on_unicode_error=...
    ):  # -> tuple[Unknown, NDArray[Unknown]]:
        """
        Get the entire list of words of the dictionary optionally
        including the frequency of the individual words. This
        does not include any subwords. For that please consult
        the function get_subwords.
        """
        ...
    def get_labels(
        self, include_freq=..., on_unicode_error=...
    ):  # -> tuple[Unknown, NDArray[Unknown]]:
        """
        Get the entire list of labels of the dictionary optionally
        including the frequency of the individual labels. Unsupervised
        models use words as labels, which is why get_labels
        will call and return get_words for this type of
        model.
        """
        ...
    def get_line(self, text, on_unicode_error=...):
        """
        Split a line of text into words and labels. Labels must start with
        the prefix used to create the model (__label__ by default).
        """
        ...
    def save_model(self, path):  # -> None:
        """Save the model to the given path"""
        ...
    def test(self, path, k=..., threshold=...):
        """Evaluate supervised model using file given by path"""
        ...
    def test_label(self, path, k=..., threshold=...):
        """
        Return the precision and recall score for each label.

        The returned value is a dictionary, where the key is the label.
        For example:
        f.test_label(...)
        {'__label__italian-cuisine' : {'precision' : 0.7, 'recall' : 0.74}}
        """
        ...
    def get_meter(self, path, k=...):  # -> _Meter:
        ...
    def quantize(
        self,
        input=...,
        qout=...,
        cutoff=...,
        retrain=...,
        epoch=...,
        lr=...,
        thread=...,
        verbose=...,
        dsub=...,
        qnorm=...,
    ):  # -> None:
        """
        Quantize the model reducing the size of the model and
        it's memory footprint.
        """
        ...
    def set_matrices(self, input_matrix, output_matrix):  # -> None:
        """
        Set input and output matrices. This function assumes you know what you
        are doing.
        """
        ...
    @property
    def words(self):  # -> tuple[Unknown, NDArray[Unknown]]:
        ...
    @property
    def labels(self):  # -> tuple[Unknown, NDArray[Unknown]]:
        ...
    def __getitem__(self, word):  # -> NDArray[Unknown]:
        ...
    def __contains__(self, word):  # -> bool:
        ...

def tokenize(text):
    """Given a string of text, tokenize it and return a list of tokens"""
    ...

def load_model(path):  # -> _FastText:
    """Load a model given a filepath and return a model object."""
    ...

unsupervised_default = ...

def read_args(
    arg_list, arg_dict, arg_names, default_values
):  # -> tuple[dict[Unknown, Unknown], set[Unknown]]:
    ...

def train_supervised(*kargs, **kwargs):  # -> _FastText:
    """
    Train a supervised model and return a model object.

    input must be a filepath. The input text does not need to be tokenized
    as per the tokenize function, but it must be preprocessed and encoded
    as UTF-8. You might want to consult standard preprocessing scripts such
    as tokenizer.perl mentioned here: http://www.statmt.org/wmt07/baseline.html

    The input file must must contain at least one label per line. For an
    example consult the example datasets which are part of the fastText
    repository such as the dataset pulled by classification-example.sh.
    """
    ...

def train_unsupervised(*kargs, **kwargs):  # -> _FastText:
    """
    Train an unsupervised model and return a model object.

    input must be a filepath. The input text does not need to be tokenized
    as per the tokenize function, but it must be preprocessed and encoded
    as UTF-8. You might want to consult standard preprocessing scripts such
    as tokenizer.perl mentioned here: http://www.statmt.org/wmt07/baseline.html

    The input field must not contain any labels or use the specified label prefix
    unless it is ok for those words to be ignored. For an example consult the
    dataset pulled by the example script word-vector-example.sh, which is
    part of the fastText repository.
    """
    ...

def cbow(*kargs, **kwargs): ...
def skipgram(*kargs, **kwargs): ...
def supervised(*kargs, **kwargs): ...
