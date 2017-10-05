#include "sbwutil.h"

#include <SBW/DataBlockReader.h>
#include <SBW/DataBlockWriter.h>
#include <SBW/sbwplusbasictypes.h>
#include <matrix.h>
#include <complex.h>
#include "util.h"

#include <vector>

using namespace LIB_LA;
using namespace SBW_CLAPACK;
using namespace SystemsBiologyWorkbench;

void SBWutil::AddEmptyDoubleMatrix(SystemsBiologyWorkbench::DataBlockWriter &oWriter)
{
		double** oBuffer = (double**)malloc(sizeof(double*)*1);
		oBuffer[0] = (double*)malloc(sizeof(double)*1);
		oWriter.add(0, 0, oBuffer);
		free(oBuffer[0]);
		free(oBuffer);
}
std::vector< SystemsBiologyWorkbench::SBWComplex > SBWutil::ConvertComplexToSBW(std::vector <  LIB_LA::Complex > & oVector)
{
	std::vector< SBWComplex > oResult;
	std::vector < Complex >::iterator oIter;
	for(oIter = oVector.begin(); oIter != oVector.end(); oIter++)
	{
		SBWComplex complex;
		complex.dReal = (*(oIter)).getReal();
		complex.dImag = (*(oIter)).getImag();
		oResult.push_back( complex );
	}
	return oResult;
}

std::vector< LIB_LA::Complex > SBWutil::ConvertSBWToComplex(std::vector <  SystemsBiologyWorkbench::SBWComplex > & oVector)
{
	std::vector< Complex > oResult;
	std::vector < SBWComplex >::iterator oIter;
	for(oIter = oVector.begin(); oIter != oVector.end(); oIter++)
	{
		Complex complex((*(oIter)).dReal, (*(oIter)).dImag);
		oResult.push_back( complex );
	}
	return oResult;

}


void SBWutil::AddToWriter(LIB_LA::DoubleMatrix& oMatrix, SystemsBiologyWorkbench::DataBlockWriter &oWriter)
{
	int nRows = oMatrix.numRows();
	int nCols = oMatrix.numCols();

	double** oBuffer = NULL; 

	if (nRows * nCols > 0)	
	{
		oBuffer = oMatrix.get2DMatrix(nRows, nCols);

		oWriter.add(nRows, nCols, oBuffer);

		FREE_2D_ARRAY(oBuffer,nRows);
	}
	else
	{
		oBuffer = (double**)malloc(sizeof(double*)*1);
		oBuffer[0] = (double*)malloc(sizeof(double)*1);
		oWriter.add(nRows, nCols, oBuffer);
		free(oBuffer[0]);
		free(oBuffer);
	}
}
void SBWutil::AddToWriter(LIB_LA::IntMatrix& oMatrix, SystemsBiologyWorkbench::DataBlockWriter &oWriter)
{
	int nRows = oMatrix.numRows();
	int nCols = oMatrix.numCols();

	int** oBuffer = NULL; 

	if (nRows * nCols > 0)	
	{
		oBuffer = oMatrix.get2DMatrix(nRows, nCols);

		oWriter.add(nRows, nCols, oBuffer);

		FREE_2D_ARRAY(oBuffer,nRows);
	}
	else
	{
		oBuffer = (int**)malloc(sizeof(int*)*1);
		oBuffer[0] = (int*)malloc(sizeof(int)*1);
		oWriter.add(nRows, nCols, oBuffer);
		free(oBuffer[0]);
		free(oBuffer);
	}
}

void SBWutil::AddToWriter(LIB_LA::ComplexMatrix &oMatrix, SystemsBiologyWorkbench::DataBlockWriter &oWriter)
{
	int nRows = oMatrix.numRows();
	int nCols = oMatrix.numCols();

	SBWComplex** oBuffer = NULL; 

	if (nRows * nCols > 0)	
	{
		oBuffer = (SBWComplex**) malloc(sizeof(SBWComplex*)*nRows);
		for (int i = 0; i < nRows; i++)
		{
			oBuffer[i] = (SBWComplex*) malloc(sizeof(SBWComplex)*nCols);
		}
		for (int i = 0; i < nRows; i++)
		{
			for (int j = 0; j < nCols; j++)
			{
				SBWComplex complex; 
				complex.dReal = oMatrix(i,j).getReal();
				complex.dImag = oMatrix(i,j).getImag();
				oBuffer[i][j] = complex;
			}
		}			

		oWriter.add(nRows, nCols, oBuffer);

		FREE_2D_ARRAY(oBuffer,nRows);
	}
	else
	{
		oBuffer = (SBWComplex**)malloc(sizeof(SBWComplex*)*1);
		oBuffer[0] = (SBWComplex*)malloc(sizeof(SBWComplex)*1);
		oWriter.add(nRows, nCols, oBuffer);
		free(oBuffer[0]);
		free(oBuffer);
	}
}

LIB_LA::DoubleMatrix* SBWutil::GetDoubleMatrixFromReader(SystemsBiologyWorkbench::DataBlockReader &oReader)
{
	double ** oBuffer; int cols, rows;
	oReader.get(rows , cols, oBuffer);

	LIB_LA::DoubleMatrix* oMatrix = new LIB_LA::DoubleMatrix(oBuffer, rows, cols);

	FREE_2D_ARRAY(oBuffer,rows);

	return oMatrix;

}

LIB_LA::IntMatrix* SBWutil::GetIntMatrixFromReader(SystemsBiologyWorkbench::DataBlockReader &oReader)
{
	int ** oBuffer; int cols, rows;
	oReader.get(rows , cols, oBuffer);

	LIB_LA::IntMatrix* oMatrix = new LIB_LA::IntMatrix(oBuffer, rows, cols);

	FREE_2D_ARRAY(oBuffer,rows);

	return oMatrix;

}
LIB_LA::ComplexMatrix* SBWutil::GetComplexMatrixFromReader(SystemsBiologyWorkbench::DataBlockReader &oReader)
{
	SBWComplex ** oBuffer; int cols, rows;
	oReader.get(rows , cols, oBuffer);

	LIB_LA::ComplexMatrix* oMatrix = new LIB_LA::ComplexMatrix(rows, cols);
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
            //LIB_LA::Complex complex(
			(*oMatrix)(i,j).set(oBuffer[i][j].dReal, oBuffer[i][j].dImag);
		}
	}

	FREE_2D_ARRAY(oBuffer,rows);

	return oMatrix;

}
