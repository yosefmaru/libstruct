# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_structural', [dirname(__file__)])
        except ImportError:
            import _structural
            return _structural
        if fp is not None:
            try:
                _mod = imp.load_module('_structural', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _structural = swig_import_helper()
    del swig_import_helper
else:
    import _structural
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _structural.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _structural.SwigPyIterator_value(self)
    def incr(self, n=1): return _structural.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _structural.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _structural.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _structural.SwigPyIterator_equal(self, *args)
    def copy(self): return _structural.SwigPyIterator_copy(self)
    def next(self): return _structural.SwigPyIterator_next(self)
    def __next__(self): return _structural.SwigPyIterator___next__(self)
    def previous(self): return _structural.SwigPyIterator_previous(self)
    def advance(self, *args): return _structural.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _structural.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _structural.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _structural.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _structural.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _structural.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _structural.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _structural.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class StringDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringDouble, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _structural.new_StringDouble(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _structural.StringDouble_first_set
    __swig_getmethods__["first"] = _structural.StringDouble_first_get
    if _newclass:first = _swig_property(_structural.StringDouble_first_get, _structural.StringDouble_first_set)
    __swig_setmethods__["second"] = _structural.StringDouble_second_set
    __swig_getmethods__["second"] = _structural.StringDouble_second_get
    if _newclass:second = _swig_property(_structural.StringDouble_second_get, _structural.StringDouble_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _structural.delete_StringDouble
    __del__ = lambda self : None;
StringDouble_swigregister = _structural.StringDouble_swigregister
StringDouble_swigregister(StringDouble)

class StrDoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StrDoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StrDoubleVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _structural.StrDoubleVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _structural.StrDoubleVector___nonzero__(self)
    def __bool__(self): return _structural.StrDoubleVector___bool__(self)
    def __len__(self): return _structural.StrDoubleVector___len__(self)
    def pop(self): return _structural.StrDoubleVector_pop(self)
    def __getslice__(self, *args): return _structural.StrDoubleVector___getslice__(self, *args)
    def __setslice__(self, *args): return _structural.StrDoubleVector___setslice__(self, *args)
    def __delslice__(self, *args): return _structural.StrDoubleVector___delslice__(self, *args)
    def __delitem__(self, *args): return _structural.StrDoubleVector___delitem__(self, *args)
    def __getitem__(self, *args): return _structural.StrDoubleVector___getitem__(self, *args)
    def __setitem__(self, *args): return _structural.StrDoubleVector___setitem__(self, *args)
    def append(self, *args): return _structural.StrDoubleVector_append(self, *args)
    def empty(self): return _structural.StrDoubleVector_empty(self)
    def size(self): return _structural.StrDoubleVector_size(self)
    def clear(self): return _structural.StrDoubleVector_clear(self)
    def swap(self, *args): return _structural.StrDoubleVector_swap(self, *args)
    def get_allocator(self): return _structural.StrDoubleVector_get_allocator(self)
    def begin(self): return _structural.StrDoubleVector_begin(self)
    def end(self): return _structural.StrDoubleVector_end(self)
    def rbegin(self): return _structural.StrDoubleVector_rbegin(self)
    def rend(self): return _structural.StrDoubleVector_rend(self)
    def pop_back(self): return _structural.StrDoubleVector_pop_back(self)
    def erase(self, *args): return _structural.StrDoubleVector_erase(self, *args)
    def __init__(self, *args): 
        this = _structural.new_StrDoubleVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _structural.StrDoubleVector_push_back(self, *args)
    def front(self): return _structural.StrDoubleVector_front(self)
    def back(self): return _structural.StrDoubleVector_back(self)
    def assign(self, *args): return _structural.StrDoubleVector_assign(self, *args)
    def resize(self, *args): return _structural.StrDoubleVector_resize(self, *args)
    def insert(self, *args): return _structural.StrDoubleVector_insert(self, *args)
    def reserve(self, *args): return _structural.StrDoubleVector_reserve(self, *args)
    def capacity(self): return _structural.StrDoubleVector_capacity(self)
    __swig_destroy__ = _structural.delete_StrDoubleVector
    __del__ = lambda self : None;
StrDoubleVector_swigregister = _structural.StrDoubleVector_swigregister
StrDoubleVector_swigregister(StrDoubleVector)

class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _structural.StringVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _structural.StringVector___nonzero__(self)
    def __bool__(self): return _structural.StringVector___bool__(self)
    def __len__(self): return _structural.StringVector___len__(self)
    def pop(self): return _structural.StringVector_pop(self)
    def __getslice__(self, *args): return _structural.StringVector___getslice__(self, *args)
    def __setslice__(self, *args): return _structural.StringVector___setslice__(self, *args)
    def __delslice__(self, *args): return _structural.StringVector___delslice__(self, *args)
    def __delitem__(self, *args): return _structural.StringVector___delitem__(self, *args)
    def __getitem__(self, *args): return _structural.StringVector___getitem__(self, *args)
    def __setitem__(self, *args): return _structural.StringVector___setitem__(self, *args)
    def append(self, *args): return _structural.StringVector_append(self, *args)
    def empty(self): return _structural.StringVector_empty(self)
    def size(self): return _structural.StringVector_size(self)
    def clear(self): return _structural.StringVector_clear(self)
    def swap(self, *args): return _structural.StringVector_swap(self, *args)
    def get_allocator(self): return _structural.StringVector_get_allocator(self)
    def begin(self): return _structural.StringVector_begin(self)
    def end(self): return _structural.StringVector_end(self)
    def rbegin(self): return _structural.StringVector_rbegin(self)
    def rend(self): return _structural.StringVector_rend(self)
    def pop_back(self): return _structural.StringVector_pop_back(self)
    def erase(self, *args): return _structural.StringVector_erase(self, *args)
    def __init__(self, *args): 
        this = _structural.new_StringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _structural.StringVector_push_back(self, *args)
    def front(self): return _structural.StringVector_front(self)
    def back(self): return _structural.StringVector_back(self)
    def assign(self, *args): return _structural.StringVector_assign(self, *args)
    def resize(self, *args): return _structural.StringVector_resize(self, *args)
    def insert(self, *args): return _structural.StringVector_insert(self, *args)
    def reserve(self, *args): return _structural.StringVector_reserve(self, *args)
    def capacity(self): return _structural.StringVector_capacity(self)
    __swig_destroy__ = _structural.delete_StringVector
    __del__ = lambda self : None;
StringVector_swigregister = _structural.StringVector_swigregister
StringVector_swigregister(StringVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _structural.DoubleVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _structural.DoubleVector___nonzero__(self)
    def __bool__(self): return _structural.DoubleVector___bool__(self)
    def __len__(self): return _structural.DoubleVector___len__(self)
    def pop(self): return _structural.DoubleVector_pop(self)
    def __getslice__(self, *args): return _structural.DoubleVector___getslice__(self, *args)
    def __setslice__(self, *args): return _structural.DoubleVector___setslice__(self, *args)
    def __delslice__(self, *args): return _structural.DoubleVector___delslice__(self, *args)
    def __delitem__(self, *args): return _structural.DoubleVector___delitem__(self, *args)
    def __getitem__(self, *args): return _structural.DoubleVector___getitem__(self, *args)
    def __setitem__(self, *args): return _structural.DoubleVector___setitem__(self, *args)
    def append(self, *args): return _structural.DoubleVector_append(self, *args)
    def empty(self): return _structural.DoubleVector_empty(self)
    def size(self): return _structural.DoubleVector_size(self)
    def clear(self): return _structural.DoubleVector_clear(self)
    def swap(self, *args): return _structural.DoubleVector_swap(self, *args)
    def get_allocator(self): return _structural.DoubleVector_get_allocator(self)
    def begin(self): return _structural.DoubleVector_begin(self)
    def end(self): return _structural.DoubleVector_end(self)
    def rbegin(self): return _structural.DoubleVector_rbegin(self)
    def rend(self): return _structural.DoubleVector_rend(self)
    def pop_back(self): return _structural.DoubleVector_pop_back(self)
    def erase(self, *args): return _structural.DoubleVector_erase(self, *args)
    def __init__(self, *args): 
        this = _structural.new_DoubleVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _structural.DoubleVector_push_back(self, *args)
    def front(self): return _structural.DoubleVector_front(self)
    def back(self): return _structural.DoubleVector_back(self)
    def assign(self, *args): return _structural.DoubleVector_assign(self, *args)
    def resize(self, *args): return _structural.DoubleVector_resize(self, *args)
    def insert(self, *args): return _structural.DoubleVector_insert(self, *args)
    def reserve(self, *args): return _structural.DoubleVector_reserve(self, *args)
    def capacity(self): return _structural.DoubleVector_capacity(self)
    __swig_destroy__ = _structural.delete_DoubleVector
    __del__ = lambda self : None;
DoubleVector_swigregister = _structural.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)

class StringVectorx2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVectorx2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVectorx2, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _structural.new_StringVectorx2(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _structural.StringVectorx2_first_set
    __swig_getmethods__["first"] = _structural.StringVectorx2_first_get
    if _newclass:first = _swig_property(_structural.StringVectorx2_first_get, _structural.StringVectorx2_first_set)
    __swig_setmethods__["second"] = _structural.StringVectorx2_second_set
    __swig_getmethods__["second"] = _structural.StringVectorx2_second_get
    if _newclass:second = _swig_property(_structural.StringVectorx2_second_get, _structural.StringVectorx2_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _structural.delete_StringVectorx2
    __del__ = lambda self : None;
StringVectorx2_swigregister = _structural.StringVectorx2_swigregister
StringVectorx2_swigregister(StringVectorx2)

class DoubleMatrixStringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleMatrixStringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleMatrixStringVector, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _structural.new_DoubleMatrixStringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _structural.DoubleMatrixStringVector_first_set
    __swig_getmethods__["first"] = _structural.DoubleMatrixStringVector_first_get
    if _newclass:first = _swig_property(_structural.DoubleMatrixStringVector_first_get, _structural.DoubleMatrixStringVector_first_set)
    __swig_setmethods__["second"] = _structural.DoubleMatrixStringVector_second_set
    __swig_getmethods__["second"] = _structural.DoubleMatrixStringVector_second_get
    if _newclass:second = _swig_property(_structural.DoubleMatrixStringVector_second_get, _structural.DoubleMatrixStringVector_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _structural.delete_DoubleMatrixStringVector
    __del__ = lambda self : None;
DoubleMatrixStringVector_swigregister = _structural.DoubleMatrixStringVector_swigregister
DoubleMatrixStringVector_swigregister(DoubleMatrixStringVector)

class LibStructural(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LibStructural, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LibStructural, name)
    __repr__ = _swig_repr
    def loadStoichiometryMatrix(self, *args): return _structural.LibStructural_loadStoichiometryMatrix(self, *args)
    def loadSpecies(self, *args): return _structural.LibStructural_loadSpecies(self, *args)
    def loadReactionNames(self, *args): return _structural.LibStructural_loadReactionNames(self, *args)
    def loadSBMLFromString(self, *args): return _structural.LibStructural_loadSBMLFromString(self, *args)
    def loadSBMLFromFile(self, *args): return _structural.LibStructural_loadSBMLFromFile(self, *args)
    def loadSBMLwithTests(self, *args): return _structural.LibStructural_loadSBMLwithTests(self, *args)
    def analyzeWithQR(self): return _structural.LibStructural_analyzeWithQR(self)
    def analyzeWithLU(self): return _structural.LibStructural_analyzeWithLU(self)
    def analyzeWithLUandRunTests(self): return _structural.LibStructural_analyzeWithLUandRunTests(self)
    def analyzeWithFullyPivotedLU(self): return _structural.LibStructural_analyzeWithFullyPivotedLU(self)
    def analyzeWithFullyPivotedLUwithTests(self): return _structural.LibStructural_analyzeWithFullyPivotedLUwithTests(self)
    def getL0Matrix(self): return _structural.LibStructural_getL0Matrix(self)
    def getNrMatrix(self): return _structural.LibStructural_getNrMatrix(self)
    def getFullyReorderedNrMatrix(self): return _structural.LibStructural_getFullyReorderedNrMatrix(self)
    def getColumnReorderedNrMatrix(self): return _structural.LibStructural_getColumnReorderedNrMatrix(self)
    def getNICMatrix(self): return _structural.LibStructural_getNICMatrix(self)
    def getNDCMatrix(self): return _structural.LibStructural_getNDCMatrix(self)
    def getN0Matrix(self): return _structural.LibStructural_getN0Matrix(self)
    def getLinkMatrix(self): return _structural.LibStructural_getLinkMatrix(self)
    def getK0Matrix(self): return _structural.LibStructural_getK0Matrix(self)
    def getKMatrix(self): return _structural.LibStructural_getKMatrix(self)
    def getGammaMatrix(self): return _structural.LibStructural_getGammaMatrix(self)
    def getGammaMatrixGJ(self, *args): return _structural.LibStructural_getGammaMatrixGJ(self, *args)
    def getStoichiometryMatrix(self): return _structural.LibStructural_getStoichiometryMatrix(self)
    def getReorderedStoichiometryMatrix(self): return _structural.LibStructural_getReorderedStoichiometryMatrix(self)
    def getFullyReorderedStoichiometryMatrix(self): return _structural.LibStructural_getFullyReorderedStoichiometryMatrix(self)
    def getReorderedSpecies(self): return _structural.LibStructural_getReorderedSpecies(self)
    def getSpecies(self): return _structural.LibStructural_getSpecies(self)
    def getReorderedSpeciesNamesList(self): return _structural.LibStructural_getReorderedSpeciesNamesList(self)
    def getIndependentSpecies(self): return _structural.LibStructural_getIndependentSpecies(self)
    def getIndependentSpeciesNamesList(self): return _structural.LibStructural_getIndependentSpeciesNamesList(self)
    def getDependentSpecies(self): return _structural.LibStructural_getDependentSpecies(self)
    def getDependentSpeciesNamesList(self): return _structural.LibStructural_getDependentSpeciesNamesList(self)
    def getReactions(self): return _structural.LibStructural_getReactions(self)
    def getIndependentReactionIds(self): return _structural.LibStructural_getIndependentReactionIds(self)
    def getDependentReactionIds(self): return _structural.LibStructural_getDependentReactionIds(self)
    def getReactionsNamesList(self): return _structural.LibStructural_getReactionsNamesList(self)
    def getReorderedReactions(self): return _structural.LibStructural_getReorderedReactions(self)
    def getConservedLaws(self): return _structural.LibStructural_getConservedLaws(self)
    def getConservedSums(self): return _structural.LibStructural_getConservedSums(self)
    def getInitialConditions(self): return _structural.LibStructural_getInitialConditions(self)
    def validateStructuralMatrices(self): return _structural.LibStructural_validateStructuralMatrices(self)
    def getTestDetails(self): return _structural.LibStructural_getTestDetails(self)
    def getModelName(self): return _structural.LibStructural_getModelName(self)
    def getNumSpecies(self): return _structural.LibStructural_getNumSpecies(self)
    def getNumIndSpecies(self): return _structural.LibStructural_getNumIndSpecies(self)
    def getNumDepSpecies(self): return _structural.LibStructural_getNumDepSpecies(self)
    def getNumReactions(self): return _structural.LibStructural_getNumReactions(self)
    def getNumIndReactions(self): return _structural.LibStructural_getNumIndReactions(self)
    def getNumDepReactions(self): return _structural.LibStructural_getNumDepReactions(self)
    def getRank(self): return _structural.LibStructural_getRank(self)
    def getNmatrixSparsity(self): return _structural.LibStructural_getNmatrixSparsity(self)
    def setTolerance(self, *args): return _structural.LibStructural_setTolerance(self, *args)
    def getTolerance(self): return _structural.LibStructural_getTolerance(self)
    def __init__(self): 
        this = _structural.new_LibStructural()
        try: self.this.append(this)
        except: self.this = this
    __swig_getmethods__["getInstance"] = lambda x: _structural.LibStructural_getInstance
    if _newclass:getInstance = staticmethod(_structural.LibStructural_getInstance)
    def findPositiveGammaMatrix(self, *args): return _structural.LibStructural_findPositiveGammaMatrix(self, *args)
    def getColumnReorderedNrMatrixLabels(self): return _structural.LibStructural_getColumnReorderedNrMatrixLabels(self)
    def getGammaMatrixLabels(self): return _structural.LibStructural_getGammaMatrixLabels(self)
    def getK0MatrixLabels(self): return _structural.LibStructural_getK0MatrixLabels(self)
    def getKMatrixLabels(self): return _structural.LibStructural_getKMatrixLabels(self)
    def getL0MatrixLabels(self): return _structural.LibStructural_getL0MatrixLabels(self)
    def getLinkMatrixLabels(self): return _structural.LibStructural_getLinkMatrixLabels(self)
    def getN0MatrixLabels(self): return _structural.LibStructural_getN0MatrixLabels(self)
    def getNDCMatrixLabels(self): return _structural.LibStructural_getNDCMatrixLabels(self)
    def getNICMatrixLabels(self): return _structural.LibStructural_getNICMatrixLabels(self)
    def getNrMatrixLabels(self): return _structural.LibStructural_getNrMatrixLabels(self)
    def getStoichiometryMatrixLabels(self): return _structural.LibStructural_getStoichiometryMatrixLabels(self)
    def getFullyReorderedStoichiometryMatrixLabels(self): return _structural.LibStructural_getFullyReorderedStoichiometryMatrixLabels(self)
    def getReorderedStoichiometryMatrixLabels(self): return _structural.LibStructural_getReorderedStoichiometryMatrixLabels(self)
    __swig_destroy__ = _structural.delete_LibStructural
    __del__ = lambda self : None;
LibStructural_swigregister = _structural.LibStructural_swigregister
LibStructural_swigregister(LibStructural)

def LibStructural_getInstance():
  return _structural.LibStructural_getInstance()
LibStructural_getInstance = _structural.LibStructural_getInstance

class complexArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, complexArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, complexArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _structural.new_complexArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _structural.delete_complexArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _structural.complexArray___getitem__(self, *args)
    def __setitem__(self, *args): return _structural.complexArray___setitem__(self, *args)
    def cast(self): return _structural.complexArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _structural.complexArray_frompointer
    if _newclass:frompointer = staticmethod(_structural.complexArray_frompointer)
complexArray_swigregister = _structural.complexArray_swigregister
complexArray_swigregister(complexArray)

def complexArray_frompointer(*args):
  return _structural.complexArray_frompointer(*args)
complexArray_frompointer = _structural.complexArray_frompointer

class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _structural.new_doubleArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _structural.delete_doubleArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _structural.doubleArray___getitem__(self, *args)
    def __setitem__(self, *args): return _structural.doubleArray___setitem__(self, *args)
    def cast(self): return _structural.doubleArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _structural.doubleArray_frompointer
    if _newclass:frompointer = staticmethod(_structural.doubleArray_frompointer)
doubleArray_swigregister = _structural.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(*args):
  return _structural.doubleArray_frompointer(*args)
doubleArray_frompointer = _structural.doubleArray_frompointer

class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _structural.new_intArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _structural.delete_intArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _structural.intArray___getitem__(self, *args)
    def __setitem__(self, *args): return _structural.intArray___setitem__(self, *args)
    def cast(self): return _structural.intArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _structural.intArray_frompointer
    if _newclass:frompointer = staticmethod(_structural.intArray_frompointer)
intArray_swigregister = _structural.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(*args):
  return _structural.intArray_frompointer(*args)
intArray_frompointer = _structural.intArray_frompointer

class DoubleMatrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleMatrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleMatrix, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_Rows"] = _structural.DoubleMatrix__Rows_set
    __swig_getmethods__["_Rows"] = _structural.DoubleMatrix__Rows_get
    if _newclass:_Rows = _swig_property(_structural.DoubleMatrix__Rows_get, _structural.DoubleMatrix__Rows_set)
    __swig_setmethods__["_Cols"] = _structural.DoubleMatrix__Cols_set
    __swig_getmethods__["_Cols"] = _structural.DoubleMatrix__Cols_get
    if _newclass:_Cols = _swig_property(_structural.DoubleMatrix__Cols_get, _structural.DoubleMatrix__Cols_set)
    __swig_setmethods__["_Array"] = _structural.DoubleMatrix__Array_set
    __swig_getmethods__["_Array"] = _structural.DoubleMatrix__Array_get
    if _newclass:_Array = _swig_property(_structural.DoubleMatrix__Array_get, _structural.DoubleMatrix__Array_set)
    def __init__(self, *args): 
        this = _structural.new_DoubleMatrix(*args)
        try: self.this.append(this)
        except: self.this = this
    def getArray(self): return _structural.DoubleMatrix_getArray(self)
    def getCopy(self, transpose=False): return _structural.DoubleMatrix_getCopy(self, transpose)
    def initializeFrom2DMatrix(self, *args): return _structural.DoubleMatrix_initializeFrom2DMatrix(self, *args)
    def initializeFromConst2DMatrix(self, *args): return _structural.DoubleMatrix_initializeFromConst2DMatrix(self, *args)
    __swig_destroy__ = _structural.delete_DoubleMatrix
    __del__ = lambda self : None;
    def get2DMatrix(self, *args): return _structural.DoubleMatrix_get2DMatrix(self, *args)
    def swapRows(self, *args): return _structural.DoubleMatrix_swapRows(self, *args)
    def swapCols(self, *args): return _structural.DoubleMatrix_swapCols(self, *args)
    def resize(self, *args): return _structural.DoubleMatrix_resize(self, *args)
    def getTranspose(self): return _structural.DoubleMatrix_getTranspose(self)
    def size(self): return _structural.DoubleMatrix_size(self)
    def numRows(self): return _structural.DoubleMatrix_numRows(self)
    def numCols(self): return _structural.DoubleMatrix_numCols(self)
    def __call__(self, *args): return _structural.DoubleMatrix___call__(self, *args)
    def get(self, *args): return _structural.DoubleMatrix_get(self, *args)
    def set(self, *args): return _structural.DoubleMatrix_set(self, *args)
    def toNumpy(self):
    		import numpy as np
    		result = np.zeros((self.numRows(), self.numCols()))
    		for i in range(self.numRows()):
    				for j in range(self.numCols()):
    						result[i,j] = self.get(i,j)
    		return result
    def __repr__(self):
    	return self.toNumpy().__repr__()
    def getFullyReorderedN0StoichiometryMatrix(self):
    	N = self.getFullyReorderedStoichiometryMatrix().toNumpy()
    	N_rowLen = len(N)
    	Nr = self.getFullyReorderedNrMatrix().toNumpy()
    	Nr_rowLen = len(Nr)
    	N0_rowLen = N_rowLen - Nr_rowLen
    	N0StoichMrx = StoichMrx[0:N0_rowLen]
    	return N0StoichMrx

DoubleMatrix_swigregister = _structural.DoubleMatrix_swigregister
DoubleMatrix_swigregister(DoubleMatrix)

class IntMatrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntMatrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntMatrix, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_Rows"] = _structural.IntMatrix__Rows_set
    __swig_getmethods__["_Rows"] = _structural.IntMatrix__Rows_get
    if _newclass:_Rows = _swig_property(_structural.IntMatrix__Rows_get, _structural.IntMatrix__Rows_set)
    __swig_setmethods__["_Cols"] = _structural.IntMatrix__Cols_set
    __swig_getmethods__["_Cols"] = _structural.IntMatrix__Cols_get
    if _newclass:_Cols = _swig_property(_structural.IntMatrix__Cols_get, _structural.IntMatrix__Cols_set)
    __swig_setmethods__["_Array"] = _structural.IntMatrix__Array_set
    __swig_getmethods__["_Array"] = _structural.IntMatrix__Array_get
    if _newclass:_Array = _swig_property(_structural.IntMatrix__Array_get, _structural.IntMatrix__Array_set)
    def __init__(self, *args): 
        this = _structural.new_IntMatrix(*args)
        try: self.this.append(this)
        except: self.this = this
    def getArray(self): return _structural.IntMatrix_getArray(self)
    def getCopy(self, transpose=False): return _structural.IntMatrix_getCopy(self, transpose)
    def initializeFrom2DMatrix(self, *args): return _structural.IntMatrix_initializeFrom2DMatrix(self, *args)
    def initializeFromConst2DMatrix(self, *args): return _structural.IntMatrix_initializeFromConst2DMatrix(self, *args)
    __swig_destroy__ = _structural.delete_IntMatrix
    __del__ = lambda self : None;
    def get2DMatrix(self, *args): return _structural.IntMatrix_get2DMatrix(self, *args)
    def swapRows(self, *args): return _structural.IntMatrix_swapRows(self, *args)
    def swapCols(self, *args): return _structural.IntMatrix_swapCols(self, *args)
    def resize(self, *args): return _structural.IntMatrix_resize(self, *args)
    def getTranspose(self): return _structural.IntMatrix_getTranspose(self)
    def size(self): return _structural.IntMatrix_size(self)
    def numRows(self): return _structural.IntMatrix_numRows(self)
    def numCols(self): return _structural.IntMatrix_numCols(self)
    def __call__(self, *args): return _structural.IntMatrix___call__(self, *args)
    def get(self, *args): return _structural.IntMatrix_get(self, *args)
    def set(self, *args): return _structural.IntMatrix_set(self, *args)
    def toNumpy(self):
    		import numpy as np
    		result = np.zeros((self.numRows(), self.numCols()), dtype=np.int)
    		for i in range(self.numRows()):
    				for j in range(self.numCols()):
    						result[i,j] = self.get(i,j)
    		return result
    def __repr__(self):
    	return self.toNumpy().__repr__()
    def getFullyReorderedN0StoichiometryMatrix(self):
    	N = self.getFullyReorderedStoichiometryMatrix().toNumpy()
    	N_rowLen = len(N)
    	Nr = self.getFullyReorderedNrMatrix().toNumpy()
    	Nr_rowLen = len(Nr)
    	N0_rowLen = N_rowLen - Nr_rowLen
    	N0StoichMrx = StoichMrx[0:N0_rowLen]
    	return N0StoichMrx

IntMatrix_swigregister = _structural.IntMatrix_swigregister
IntMatrix_swigregister(IntMatrix)

class ComplexMatrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ComplexMatrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ComplexMatrix, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_Rows"] = _structural.ComplexMatrix__Rows_set
    __swig_getmethods__["_Rows"] = _structural.ComplexMatrix__Rows_get
    if _newclass:_Rows = _swig_property(_structural.ComplexMatrix__Rows_get, _structural.ComplexMatrix__Rows_set)
    __swig_setmethods__["_Cols"] = _structural.ComplexMatrix__Cols_set
    __swig_getmethods__["_Cols"] = _structural.ComplexMatrix__Cols_get
    if _newclass:_Cols = _swig_property(_structural.ComplexMatrix__Cols_get, _structural.ComplexMatrix__Cols_set)
    __swig_setmethods__["_Array"] = _structural.ComplexMatrix__Array_set
    __swig_getmethods__["_Array"] = _structural.ComplexMatrix__Array_get
    if _newclass:_Array = _swig_property(_structural.ComplexMatrix__Array_get, _structural.ComplexMatrix__Array_set)
    def __init__(self, *args): 
        this = _structural.new_ComplexMatrix(*args)
        try: self.this.append(this)
        except: self.this = this
    def getArray(self): return _structural.ComplexMatrix_getArray(self)
    def getCopy(self, transpose=False): return _structural.ComplexMatrix_getCopy(self, transpose)
    def initializeFrom2DMatrix(self, *args): return _structural.ComplexMatrix_initializeFrom2DMatrix(self, *args)
    def initializeFromConst2DMatrix(self, *args): return _structural.ComplexMatrix_initializeFromConst2DMatrix(self, *args)
    __swig_destroy__ = _structural.delete_ComplexMatrix
    __del__ = lambda self : None;
    def get2DMatrix(self, *args): return _structural.ComplexMatrix_get2DMatrix(self, *args)
    def swapRows(self, *args): return _structural.ComplexMatrix_swapRows(self, *args)
    def swapCols(self, *args): return _structural.ComplexMatrix_swapCols(self, *args)
    def resize(self, *args): return _structural.ComplexMatrix_resize(self, *args)
    def getTranspose(self): return _structural.ComplexMatrix_getTranspose(self)
    def size(self): return _structural.ComplexMatrix_size(self)
    def numRows(self): return _structural.ComplexMatrix_numRows(self)
    def numCols(self): return _structural.ComplexMatrix_numCols(self)
    def __call__(self, *args): return _structural.ComplexMatrix___call__(self, *args)
    def get(self, *args): return _structural.ComplexMatrix_get(self, *args)
    def set(self, *args): return _structural.ComplexMatrix_set(self, *args)
    def toNumpy(self):
    		import numpy as np
    		result = np.zeros((self.numRows(), self.numCols()), dtype=np.complex_)
    		for i in range(self.numRows()):
    				for j in range(self.numCols()):
    						result[i,j] = self.getReal(i,j) + self.getImag(i,j)*1j
    		return result
    def __repr__(self):
    		return self.toNumpy().__repr__()

ComplexMatrix_swigregister = _structural.ComplexMatrix_swigregister
ComplexMatrix_swigregister(ComplexMatrix)

# This file is compatible with both classic and new-style classes.


