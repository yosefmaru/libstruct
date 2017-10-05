#ifndef SBW_CLAPACK_SBWCLAPACK_H
#define SBW_CLAPACK_SBWCLAPACK_H

#include <SBW/Module.h>
#include <SBW/MethodTable.h>
#include <SBW/DataBlockReader.h>
#include <SBW/DataBlockWriter.h>

#include "libla.h"

namespace SBW_CLAPACK
{

	class SBWclapack
	{
	public: 
		SBWclapack();

	protected:
		DataBlockWriter setTolerance(Module /*from*/, DataBlockReader reader);
		DataBlockWriter getEigenValues(Module /*from*/, DataBlockReader reader);
		DataBlockWriter ZgetEigenValues(Module /*from*/, DataBlockReader reader);
		DataBlockWriter getQR(Module /*from*/, DataBlockReader reader);
		DataBlockWriter getQRWithPivot(Module /*from*/, DataBlockReader reader);
		DataBlockWriter getSingularValsBySVD(Module /*from*/, DataBlockReader reader);
		DataBlockWriter getLUwithFullPivoting(Module /*from*/, DataBlockReader reader);
		DataBlockWriter getLU(Module /*from*/, DataBlockReader reader);
		DataBlockWriter inverse(Module /*from*/, DataBlockReader reader);
		DataBlockWriter Zinverse(Module /*from*/, DataBlockReader reader);

	private:

		LIB_LA::LibLA *_Instance;

	public:
		// ----------------------------------------------------------------------------
		// Register methods with SBW
		// ----------------------------------------------------------------------------
		static void registerMethods (SystemsBiologyWorkbench::MethodTable<SBWclapack> &table) 
		{	
			table.addMethod (&SBWclapack::setTolerance,          "void setTolerance (double)", false, "Set tolerance for numerical computations.");
			table.addMethod (&SBWclapack::getEigenValues,        "complex[] getEigenValues (double[][])", false, "Compute the complex eigenvalues of a real matrix.");
			table.addMethod (&SBWclapack::ZgetEigenValues,       "complex[] ZgetEigenValues (complex[][])", false, "Compute the complex eigenvalues of a complex matrix.");
			table.addMethod (&SBWclapack::getQRWithPivot,        "{} getQRWithPivot (double[][])", false, "Compute QR decomposition of a real matrix using Householder method with Pivoting.");
			table.addMethod (&SBWclapack::getQR,                 "{} getQR (double[][])", false, "Compute QR decomposition of a real matrix without pivoting.");
			table.addMethod (&SBWclapack::getSingularValsBySVD,  "double[] getSingularValsBySVD (double[][])", false, "Find the singular values of a real matrix using Singular Value Decomposition.");
			table.addMethod (&SBWclapack::getLUwithFullPivoting, "{} getLUwithFullPivoting (double[][])", false, "Compute LU decomposition of a real matrix with full pivoting.");
			table.addMethod (&SBWclapack::getLU,                 "{} getLU (double[][])", false, "Compute LU decomposition of a real matrix with partial pivoting.");
			table.addMethod (&SBWclapack::inverse,               "double[][] inverse (double[][])", false, "Compute the inverse of a real matrix.");
			table.addMethod (&SBWclapack::Zinverse,              "complex[][] Zinverse (complex[][])", false, "Compute the inverse of a complex matrix.");
		}

	};

}
#endif

