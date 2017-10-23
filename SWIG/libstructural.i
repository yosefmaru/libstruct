%module structural

// #pragma SWIG nowarn=516

%inline
%{
#include "libstructural.h"
#include "util.h"
#include "libla.h"
%}

%include "carrays.i"
%include "typemaps.i"
%include "stl.i"

%template(StringDouble) std::pair<std::string,double>;
%template(StrDoubleVector) std::vector< std::pair<std::string,double> >;
%template(StringVector) std::vector<std::string>;
%template(DoubleVector) std::vector<double>;
%template(StringVectorx2) std::pair< std::vector<std::string>, std::vector<std::string> >;

%include "../include/matrix.h"

%template(DoubleMatrixStringVector) std::pair<LIB_LA::DoubleMatrix*,  std::vector< std::string> >;

// http://swig.10945.n7.nabble.com/replacing-a-real-class-method-with-SWIG-version-td11418.html
%extend LIB_STRUCTURAL::LibStructural {
	std::pair<LIB_LA::DoubleMatrix*,  std::vector< std::string> > findPositiveGammaMatrix(LIB_LA::DoubleMatrix* stoichiometry, std::vector< std::string> rowLabels) {
		return std::make_pair(self->findPositiveGammaMatrix(*stoichiometry, rowLabels), rowLabels);
	}

	std::pair< std::vector<std::string>, std::vector<std::string> > getColumnReorderedNrMatrixLabels() {
		std::vector<std::string> rows;
		std::vector<std::string> cols;
		self->getColumnReorderedNrMatrixLabels(rows, cols);
		return std::make_pair(rows, cols);
	}

	std::pair< std::vector<std::string>, std::vector<std::string> > getGammaMatrixLabels() {
		std::vector<std::string> rows;
		std::vector<std::string> cols;
		self->getGammaMatrixLabels(rows, cols);
		return std::make_pair(rows, cols);
	}
}

%ignore LIB_STRUCTURAL::LibStructural::findPositiveGammaMatrix;
%ignore LIB_STRUCTURAL::LibStructural::getColumnReorderedNrMatrixLabels;
%ignore LIB_STRUCTURAL::LibStructural::getGammaMatrixLabels;

%include "../include/libstructural.h"

%rename(assign) operator=;
%rename(add) operator+;
%rename(sub) operator-;
%rename(div) operator/;
%rename(mult) operator*;
%ignore operator<<;
%ignore operator();
%ignore operator[];

%ignore getReal;
%ignore setReal;
%ignore getImag;
%ignore setImag;



%inline
%{
#include "..\include\complex.h"
%}

%array_class(LIB_LA::Complex, complexArray);
%array_class(double, doubleArray);
%array_class(int, intArray);
%array_function(LIB_LA::Complex, complexArray);
%array_function(double, doubleArray);
%array_function(int, intArray);

using LIB_LA::Matrix;

%template(DoubleMatrix) LIB_LA::Matrix<double>;
%template(IntMatrix) LIB_LA::Matrix<int>;
%template(ComplexMatrix) LIB_LA::Matrix<LIB_LA::Complex>;

// #ifdef SWIGCSHARP
// %template(StringDouble) std::pair< std::string, double >;
// %template(StringDoubleVector) std::vector< std::pair< std::string, double > >;
// #endif

%extend LIB_LA::Matrix<double>
{
	virtual double get(const unsigned int row, const unsigned int col)
  {
		return *(self->_Array + row * self->_Cols + col);
	}

	virtual void set(const unsigned int row, const unsigned int col, double value)
  {
		(*self)(row,col) = value;
	}

%pythoncode %{
		def toNumpy(self):
				import numpy as np
				result = np.zeros((self.numRows(), self.numCols()))
				for i in range(self.numRows()):
						for j in range(self.numCols()):
								result[i,j] = self.get(i,j)
				return result
		def __repr__(self):
				return self.toNumpy().__repr__()
%}
}

%extend LIB_LA::Matrix<int>
{
	virtual int get(const unsigned int row, const unsigned int col)
    {
		return (*self)(row,col);
	}

	virtual void set(const unsigned int row, const unsigned int col, int value)
    {
		(*self)(row,col) = value;
	}

%pythoncode %{
		def toNumpy(self):
				import numpy as np
				result = np.zeros((self.numRows(), self.numCols()), dtype=np.int)
				for i in range(self.numRows()):
						for j in range(self.numCols()):
								result[i,j] = self.get(i,j)
				return result
		def __repr__(self):
				return self.toNumpy().__repr__()
%}
}

%extend LIB_LA::Matrix<LIB_LA::Complex>
{
	virtual LIB_LA::Complex get(const unsigned int row, const unsigned int col)
    {
		return (*self)(row,col);
	}

	virtual double getReal(const unsigned int row, const unsigned int col)
    {
		return (*self)(row,col).Real;
	}
	virtual double getImag(const unsigned int row, const unsigned int col)
    {
		return (*self)(row,col).Imag;
	}

	virtual void set(const unsigned int row, const unsigned int col, LIB_LA::Complex value)
    {
		(*self)(row,col) = value;
	}

	virtual void setReal(const unsigned int row, const unsigned int col, double value)
    {
		(*self)(row,col).Real = value;
	}
	virtual void setImag(const unsigned int row, const unsigned int col, double value)
    {
		(*self)(row,col).Imag = value;
	}

%pythoncode %{
		def toNumpy(self):
				import numpy as np
				result = np.zeros((self.numRows(), self.numCols()), dtype=np.complex_)
				for i in range(self.numRows()):
						for j in range(self.numCols()):
								result[i,j] = self.getReal(i,j) + self.getImag(i,j)*1j
				return result
		def __repr__(self):
				return self.toNumpy().__repr__()
%}
}

// %ignore LIB_STRUCTURAL::LibStructural::getInitialConditions;
// %rename (_getInitialConditions) LIB_STRUCTURAL::LibStructural::getInitialConditions;

/*%extend LIB_STRUCTURAL::LibStructural {
	std::vector< std::pair<std::string, double> > _getInitialConditions() {
		return *self->getInitialConditions();
	}
%pythoncode %{
		def getInitialConditions(*args):
				return _getInitialConditions(*args)
%}
}*/
