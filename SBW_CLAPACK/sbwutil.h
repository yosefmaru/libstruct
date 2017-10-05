#ifndef SBW_CLAPACK_SBWUTIL_H
#define SBW_CLAPACK_SBWUTIL_H

#include <SBW/DataBlockReader.h>
#include <SBW/DataBlockWriter.h>

#include <matrix.h>
#include <complex.h>
#include <vector>

namespace SBW_CLAPACK
{
	class SBWutil
	{
	public:
		static void AddToWriter(LIB_LA::DoubleMatrix & oMatrix, SystemsBiologyWorkbench::DataBlockWriter &oWriter);
		static void AddToWriter(LIB_LA::IntMatrix & oMatrix, SystemsBiologyWorkbench::DataBlockWriter &oWriter);
		static void AddToWriter(LIB_LA::ComplexMatrix & oMatrix, SystemsBiologyWorkbench::DataBlockWriter &oWriter);

		static void AddEmptyDoubleMatrix(SystemsBiologyWorkbench::DataBlockWriter &oWriter);

		static std::vector< SystemsBiologyWorkbench::SBWComplex > ConvertComplexToSBW(std::vector <  LIB_LA::Complex >& oVector);
		static std::vector< LIB_LA::Complex > ConvertSBWToComplex(std::vector <  SystemsBiologyWorkbench::SBWComplex >& oVector);

		static LIB_LA::DoubleMatrix* GetDoubleMatrixFromReader(SystemsBiologyWorkbench::DataBlockReader &oReader);
		static LIB_LA::IntMatrix* GetIntMatrixFromReader(SystemsBiologyWorkbench::DataBlockReader &oReader);
		static LIB_LA::ComplexMatrix* GetComplexMatrixFromReader(SystemsBiologyWorkbench::DataBlockReader &oReader);

	};
}

#endif


