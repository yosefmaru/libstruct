%module structural

// #pragma SWIG nowarn=516

%include "carrays.i"
%include "typemaps.i"
%include "stl.i"

%include "../include/matrix.h"

%include "../include/libstructural.h"

%inline
%{
#include "libstructural.h"
#include "util.h"
#include "libla.h"
%}

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


%template(StringVector) std::vector<std::string>;
%template(DoubleVector) std::vector<double>;

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

#ifdef SWIGCSHARP
%template(StringDouble) std::pair< std::string, double >;
%template(StringDoubleVector) std::vector< std::pair< std::string, double > >;
#endif

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
}

%extend LIB_LA::Matrix<LIB_LA::Complex>
{
	virtual LIB_LA::Complex get(const unsigned int row, const unsigned int col)
    {
		return (*self)(row,col);
	}
	virtual void set(const unsigned int row, const unsigned int col, LIB_LA::Complex value)
    {
		(*self)(row,col) = value;
	}

}
