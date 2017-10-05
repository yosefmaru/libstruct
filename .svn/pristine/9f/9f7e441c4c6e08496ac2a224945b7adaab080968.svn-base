/* Filename    : SBW_CLAPACK.cpp
* Description : SBW Interface to CLAPACK
* Author(s)   : Ravishankar  Rao Vallabhajosyula
* Organization: Keck Graduate Institute
* Created     : 2005
*
* This software is licenced under the BSD Licence.
*
* Original author:
*   Ravishankar  Rao Vallabhajosyula (Ravi_Rao@kgi.edu)
*
* Copyright (c) 2005 <Ravishankar  Rao Vallabhajosyula>
* All rights reserved
*
* Redistribution and use in source and binary forms, with or without
*  modification, are permitted provided that the following conditionsa
* are met:
* 1. Redistributions of source code must retain the above copyright
*    notice, this list of conditions and the following disclaimer.
* 2. Redistributions in binary form must reproduce the above copyright
*    notice, this list of conditions and the following disclaimer in the
*    documentation and/or other materials provided with the distribution.
* 3. The name of the author may not be used to endorse or promote products
*    derived from this software without specific prior written permission.

* THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
* IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
* OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
* IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
* INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
* NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
* DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
* THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
* (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
* THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*****************************************************************************/





/*--------------------------------------------------------------------------
* Revision History
*
* DATE         DESCRIPTION                                          AUTHOR
* ----         -----------                                          ------
* 10/28/2005   Zinverse method now throws an exception if a          Ravi
*              singular matrix is encountered on input              
* 10/28/2005   Same issue fixed in inverse method                    Ravi
*
* 11/01/2005   Help strings added for all methods                    Ravi
*
*-------------------------------------------------------------------------*/


#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <cmath>
#include <sstream>
#include <vector>

#include "SBW/SBW.h"

#include "f2c.h"
#include "clapack.h"

#include "sbwclapack.h"
#include "libla.h"
#include "matrix.h"
#include "util.h"
#include "sbwutil.h"


using namespace std;
using namespace SystemsBiologyWorkbench;
using namespace SBW_CLAPACK;
using namespace LIB_LA;


#define BEGIN_TRY try\
{//

#define END_TRY_THROW_SBW(errorMessage) }\
	catch(ApplicationException* exception)\
{\
	throw new SBWApplicationException(exception->getMessage(), exception->getDetailedMessage());\
}\
	catch(SBWException*)\
{\
	throw;\
}\
	catch(...)\
{\
	throw new SBWApplicationException(errorMessage);\
}//


SBWclapack::SBWclapack() : _Instance(LibLA::getInstance())
{
	
}

// ----------------------------------------------------------------------------
// complex[] getEigenValues (double[][])
// 
// Returns the eigenvalues of a double non-symmetric matrix.
// ----------------------------------------------------------------------------
DataBlockWriter SBWclapack::setTolerance (Module /*from*/, DataBlockReader reader) 
{	
	BEGIN_TRY;
	double tol; reader >> tol;

	_Instance->setTolerance(tol);

	return DataBlockWriter();
	END_TRY_THROW_SBW("Unexpected Exception in setTolerance");
}



// ----------------------------------------------------------------------------
// complex[] getEigenValues (double[][])
// 
// Returns the eigenvalues of a double non-symmetric matrix.
// ----------------------------------------------------------------------------
DataBlockWriter SBWclapack::getEigenValues (Module /*from*/, DataBlockReader reader) 
{	

	BEGIN_TRY;
	DoubleMatrix *oMatrix = SBWutil::GetDoubleMatrixFromReader(reader);	

	std::vector< Complex > oResult = _Instance->getEigenValues(*oMatrix);

	delete oMatrix;
	return DataBlockWriter() << SBWutil::ConvertComplexToSBW(  oResult ) ;
	END_TRY_THROW_SBW("Unexpected Exception in getEigenValues");

}


// ----------------------------------------------------------------------------
// complex[] zgetEigenValues (complex[][])
// 
// Returns the eigenvalues of a complex non-symmetric matrix.
// ----------------------------------------------------------------------------
DataBlockWriter SBWclapack::ZgetEigenValues (Module /*from*/, DataBlockReader reader) 
{

	BEGIN_TRY;

	ComplexMatrix *oMatrix = SBWutil::GetComplexMatrixFromReader(reader);	

	std::vector< LIB_LA::Complex > oResult = _Instance->ZgetEigenValues(*oMatrix);

	delete oMatrix;
	return DataBlockWriter() << SBWutil::ConvertComplexToSBW( oResult );
	END_TRY_THROW_SBW("Unexpected Exception in ZgetEigenValues");

}


// ----------------------------------------------------------------------------
// {} getQR (double[][])
// 
// Returns the QR decoposition of a matrix as a list comprising two arrays.
// These are double[][] Q and double[][] R, such that A = Q*R. Q is an orthogonal 
// matrix, and R is an upper trapezoidal matrix with zeros below diagonal. 
// ----------------------------------------------------------------------------

DataBlockWriter SBWclapack::getQR (Module /*from*/, DataBlockReader reader) 
{	
	BEGIN_TRY;
	DoubleMatrix *oMatrix = SBWutil::GetDoubleMatrixFromReader(reader);	

	std::vector< DoubleMatrix* > oResult = _Instance->getQR(*oMatrix);

	DataBlockWriter oResultList;

	for (unsigned int i = 0; i < oResult.size(); i++)
	{
		SBWutil::AddToWriter(*oResult[i],oResultList);		
		delete oResult[i];
	}

	return DataBlockWriter() << oResultList;
	END_TRY_THROW_SBW("Unexpected Exception in getQR");
}

// ----------------------------------------------------------------------------
// {} getQRWithPivot (double[][])
// 
// Returns the QR decoposition of a matrix as a list comprising three arrays.
// These are double[][] Q, double[][] R, double[][] P, where P is the permutation
// matrix, such that A*P = Q*R. Q is an orthogonal matrix, and R is an upper 
// trapezoidal matrix with zeros below diagonal. 
// ----------------------------------------------------------------------------
DataBlockWriter SBWclapack::getQRWithPivot (Module /*from*/, DataBlockReader reader) 
{	
	BEGIN_TRY;
	DoubleMatrix *oMatrix = SBWutil::GetDoubleMatrixFromReader(reader);

	std::vector< DoubleMatrix* > oResult = _Instance->getQRWithPivot(*oMatrix);

	DataBlockWriter oResultList;

	for (unsigned int i = 0; i < oResult.size(); i++)
	{
		SBWutil::AddToWriter(*oResult[i],oResultList);		
		delete oResult[i];		
	}

	return DataBlockWriter() << oResultList;
	END_TRY_THROW_SBW("Unexpected Exception in getQRwithPivot");

}

// ----------------------------------------------------------------------------
// double[] getSingularValsBySVD (double[][])
// 
// Returns the Singular Valude Decomposition of a mxn matrix.
// ----------------------------------------------------------------------------
DataBlockWriter SBWclapack::getSingularValsBySVD (Module /*from*/, DataBlockReader reader) 
{	
	BEGIN_TRY;
	DoubleMatrix *oMatrix = SBWutil::GetDoubleMatrixFromReader(reader);	

	std::vector< double > oResult = _Instance->getSingularValsBySVD(*oMatrix);

	return DataBlockWriter() << oResult;
	END_TRY_THROW_SBW("Unexpected Exception in getSingularValsBySVD");

}

// ----------------------------------------------------------------------------
// {} getLUwithFullPivoting (double[][])
// 
// Returns the LU decoposition of a matrix as a list comprising four arrays.
// These are double[][] L, double[][] U, double[][] P, and double[][] Q, where 
// P and Q are column and row permutation matrices, such that A = P*L*U*Q. L 
// is a lower triangular matrix, while U is an upper triangular matrix with 
// zeros below diagonal. Lastly getLU also returns the integer info that is 
// an output from LAPACK. This helps indentify if there are any singular 
// values on the diagonal in U matrix (pivot positions)
// ----------------------------------------------------------------------------
DataBlockWriter SBWclapack::getLUwithFullPivoting (Module /*from*/, DataBlockReader reader) 
{	
	BEGIN_TRY;
	DoubleMatrix *oMatrix = SBWutil::GetDoubleMatrixFromReader(reader);	

	LU_Result *oResult = _Instance->getLUwithFullPivoting(*oMatrix);

	DataBlockWriter oResultList;

	SBWutil::AddToWriter(*(oResult->L),oResultList);		
	SBWutil::AddToWriter(*(oResult->U),oResultList);		
	SBWutil::AddToWriter(*(oResult->P),oResultList);		
	SBWutil::AddToWriter(*(oResult->Q),oResultList);		
	oResultList << oResult->nInfo;
		 
	delete oResult; delete oMatrix;
	
	return DataBlockWriter() << oResultList;
	END_TRY_THROW_SBW("Unexpected Exception in getLUwithFullPivoting");
	
}

// ----------------------------------------------------------------------------
// {} getLU (double[][])
// 
// Returns the LU decoposition of a matrix as a list comprising three arrays.
// These are double[][] L, double[][] U, double[][] P, where P is the permutation
// matrix, such that A = P*L*U. L is a lower triangular matrix, while U is an
// upper triangular matrix with zeros below diagonal. Lastly getLU also returns
// the integer info that is an output from LAPACK. This helps indentify if there
// are any singular values on the diagonal in U matrix (pivot positions)
// ----------------------------------------------------------------------------
DataBlockWriter SBWclapack::getLU (Module /*from*/, DataBlockReader reader) 
{	
	BEGIN_TRY;
	DoubleMatrix *oMatrix = SBWutil::GetDoubleMatrixFromReader(reader);	

	LU_Result *oResult = _Instance->getLU(*oMatrix);

	DataBlockWriter oResultList;

	SBWutil::AddToWriter(*(oResult->L),oResultList);		
	SBWutil::AddToWriter(*(oResult->U),oResultList);		
	SBWutil::AddToWriter(*(oResult->P),oResultList);		
	
	oResultList << oResult->nInfo;

	delete oResult;

	return DataBlockWriter() << oResultList;
	END_TRY_THROW_SBW("Unexpected Exception in getLU");

}

// ----------------------------------------------------------------------------
// double[][] inverse (double[][])
// 
// Returns the inverse of a general matrix using LU factorization.
// ----------------------------------------------------------------------------
DataBlockWriter SBWclapack::inverse (Module /*from*/, DataBlockReader reader) 
{	
	BEGIN_TRY;
	DoubleMatrix *oMatrix = SBWutil::GetDoubleMatrixFromReader(reader);	

	DoubleMatrix *oResult = _Instance->inverse(*oMatrix);

	DataBlockWriter oResultWriter;

	SBWutil::AddToWriter(*oResult,oResultWriter);		

	delete oResult;

	return oResultWriter;
	END_TRY_THROW_SBW("Unexpected Exception in inverse");

}

// ----------------------------------------------------------------------------
// complex[][] Zinverse (complex[][])
// 
// Returns the inverse of a general complex matrix using LU factorization.
// ----------------------------------------------------------------------------
DataBlockWriter SBWclapack::Zinverse (Module /*from*/, DataBlockReader reader) 
{
	BEGIN_TRY;
	ComplexMatrix *oMatrix = SBWutil::GetComplexMatrixFromReader(reader);	

	ComplexMatrix *oResult = _Instance->Zinverse(*oMatrix);	

	DataBlockWriter oResultWriter;

	SBWutil::AddToWriter(*oResult,oResultWriter);		

	delete oResult;

	return oResultWriter;
	END_TRY_THROW_SBW("Unexpected Exception in Zinverse");

}


