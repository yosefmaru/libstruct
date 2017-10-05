#include "sbwstructural.h"
#include "libstructural.h"

#include "SBW/SBW.h"

#include "util.h"
#include "../SBW_CLAPACK/sbwutil.h"

#include <string>

using namespace std;
using namespace SBW_STRUCTURAL;
using namespace LIB_STRUCTURAL;
using namespace LIB_LA;
using namespace SBW_CLAPACK;
using namespace SystemsBiologyWorkbench;


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



DataBlockWriter SBWstructural::getName(Module /*from*/, DataBlockReader reader)
{
	return DataBlockWriter() << CONSV_NAME;
}
DataBlockWriter SBWstructural::getVersion(Module /*from*/, DataBlockReader reader)
{
	return DataBlockWriter() << CONSV_VERSION;
}
DataBlockWriter SBWstructural::getAuthor(Module /*from*/, DataBlockReader reader)
{
	return DataBlockWriter() << CONSV_AUTHOR;
}
DataBlockWriter SBWstructural::getDescription(Module /*from*/, DataBlockReader reader)
{
	return DataBlockWriter() << CONSV_DESCRIPTION;
}
DataBlockWriter SBWstructural::getDisplayName(Module /*from*/, DataBlockReader reader)
{
	return DataBlockWriter() << CONSV_DISPLAYNAME;
}
DataBlockWriter SBWstructural::getCopyright(Module /*from*/, DataBlockReader reader)
{
	return DataBlockWriter() << CONSV_COPYRIGHT;
}
DataBlockWriter SBWstructural::getURL(Module /*from*/, DataBlockReader reader)
{
	return DataBlockWriter() << CONSV_URL;
}
#ifndef NO_SBML

DataBlockWriter SBWstructural::loadSBML(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;
	string sSBML; reader >> sSBML;
	return DataBlockWriter() << _Instance->loadSBML(sSBML);
	END_TRY_THROW_SBW("Unexpected Exception in LoadSBML.");
}

DataBlockWriter SBWstructural::loadSBMLwithTests(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;
	string sSBML; reader >> sSBML;
	return DataBlockWriter() << _Instance->loadSBMLwithTests(sSBML);
	END_TRY_THROW_SBW("Unexpected Exception in loadSBMLwithTests.");
}
#endif
DataBlockWriter SBWstructural::getL0Matrix(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	LibStructural::DoubleMatrix* oMatrix = _Instance->getL0Matrix();

	DataBlockWriter oWriter;   

	if (oMatrix == NULL) SBWutil::AddEmptyDoubleMatrix(oWriter);
	else { SBWutil::AddToWriter(*oMatrix,oWriter); delete oMatrix; } 
	

	return oWriter;

	END_TRY_THROW_SBW("Unexpected Exception in getL0Matrix.");
}
DataBlockWriter SBWstructural::getNrMatrix(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	LibStructural::DoubleMatrix* oMatrix = _Instance->getNrMatrix();

	DataBlockWriter oWriter;   

	if (oMatrix == NULL) SBWutil::AddEmptyDoubleMatrix(oWriter);
	else SBWutil::AddToWriter(*oMatrix,oWriter); 

	return oWriter;

	END_TRY_THROW_SBW("Unexpected Exception in getNrMatrix.");
}
DataBlockWriter SBWstructural::getN0Matrix(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	LibStructural::DoubleMatrix* oMatrix = _Instance->getN0Matrix();

	DataBlockWriter oWriter;   

	if (oMatrix == NULL) SBWutil::AddEmptyDoubleMatrix(oWriter);
	else SBWutil::AddToWriter(*oMatrix,oWriter); 

	return oWriter;

	END_TRY_THROW_SBW("Unexpected Exception in getN0Matrix.");

}
DataBlockWriter SBWstructural::getK0Matrix(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	LibStructural::DoubleMatrix* oMatrix = _Instance->getK0Matrix();

	DataBlockWriter oWriter;   

	if (oMatrix == NULL) SBWutil::AddEmptyDoubleMatrix(oWriter);
	else SBWutil::AddToWriter(*oMatrix,oWriter); 

	return oWriter;

	END_TRY_THROW_SBW("Unexpected Exception in getK0Matrix.");

}
DataBlockWriter SBWstructural::getLinkMatrix(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	LibStructural::DoubleMatrix* oMatrix = _Instance->getLinkMatrix();

	DataBlockWriter oWriter;   

	if (oMatrix == NULL) SBWutil::AddEmptyDoubleMatrix(oWriter);
	else SBWutil::AddToWriter(*oMatrix,oWriter); 

	return oWriter;

	END_TRY_THROW_SBW("Unexpected Exception in getLinkMatrix.");

}
DataBlockWriter SBWstructural::getKMatrix(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	LibStructural::DoubleMatrix* oMatrix = _Instance->getKMatrix();

	DataBlockWriter oWriter;   

	if (oMatrix == NULL) SBWutil::AddEmptyDoubleMatrix(oWriter);
	else SBWutil::AddToWriter(*oMatrix,oWriter); 

	return oWriter;

	END_TRY_THROW_SBW("Unexpected Exception in getKMatrix.");

}
DataBlockWriter SBWstructural::getModelName(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getModelName();

	END_TRY_THROW_SBW("Unexpected Exception in getModelName.");
}
DataBlockWriter SBWstructural::getNumSpecies(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getNumSpecies();

	END_TRY_THROW_SBW("Unexpected Exception in getNumSpecies.");
}
DataBlockWriter SBWstructural::getNumIndSpecies(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getNumIndSpecies();

	END_TRY_THROW_SBW("Unexpected Exception in getNumIndSpecies.");
}
DataBlockWriter SBWstructural::getNumDepSpecies(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getNumDepSpecies();

	END_TRY_THROW_SBW("Unexpected Exception in getNumDepSpecies.");
}
DataBlockWriter SBWstructural::getNumReactions(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getNumReactions();

	END_TRY_THROW_SBW("Unexpected Exception in getNumReactions.");
}
DataBlockWriter SBWstructural::getRank(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getRank();

	END_TRY_THROW_SBW("Unexpected Exception in getRank.");
}
DataBlockWriter SBWstructural::getNmatrixSparsity(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getNmatrixSparsity();

	END_TRY_THROW_SBW("Unexpected Exception in getNmatrixSparsity.");
}
DataBlockWriter SBWstructural::getGammaMatrix(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	LibStructural::DoubleMatrix* oMatrix = _Instance->getGammaMatrix();

	DataBlockWriter oWriter;   

	if (oMatrix == NULL) SBWutil::AddEmptyDoubleMatrix(oWriter);
	else SBWutil::AddToWriter(*oMatrix,oWriter); 

	return oWriter;

	END_TRY_THROW_SBW("Unexpected Exception in getGammaMatrix.");
}
DataBlockWriter SBWstructural::getConservedSums(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getConservedSums();

	END_TRY_THROW_SBW("Unexpected Exception in getConservedSums.");
}
DataBlockWriter SBWstructural::getConservedLaws(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getConservedLaws();

	END_TRY_THROW_SBW("Unexpected Exception in getConservedLaws.");
}
DataBlockWriter SBWstructural::getReorderedSpecies(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getReorderedSpecies();

	END_TRY_THROW_SBW("Unexpected Exception in getReorderedSpecies.");
}
DataBlockWriter SBWstructural::getReorderedSpeciesNamesList(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getReorderedSpeciesNamesList();

	END_TRY_THROW_SBW("Unexpected Exception in getReorderedSpeciesNamesList.");
}
DataBlockWriter SBWstructural::getIndependentSpecies(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getIndependentSpecies();

	END_TRY_THROW_SBW("Unexpected Exception in getIndependentSpecies.");
}
DataBlockWriter SBWstructural::getIndependentSpeciesNamesList(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getIndependentSpeciesNamesList();

	END_TRY_THROW_SBW("Unexpected Exception in getIndependentSpeciesNamesList.");
}
DataBlockWriter SBWstructural::getDependentSpecies(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getDependentSpecies();

	END_TRY_THROW_SBW("Unexpected Exception in getDependentSpecies.");
}
DataBlockWriter SBWstructural::getDependentSpeciesNamesList(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getDependentSpeciesNamesList();

	END_TRY_THROW_SBW("Unexpected Exception in getDependentSpeciesNamesList.");
}
DataBlockWriter SBWstructural::getInitialConditions(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	DataBlockWriter result;

	std::vector< std::pair <std::string, double> > oResult = 
		_Instance->getInitialConditions();

	DataBlockWriter oOuter;
	std::vector< std::pair <std::string, double> >::iterator oIterator;
	for (oIterator = oResult.begin(); oIterator != oResult.end(); oIterator++)
	{
		DataBlockWriter oInner; 
		oInner << (*oIterator).first << (*oIterator).second;
		oOuter << oInner;
	}

	return result << oOuter;

	END_TRY_THROW_SBW("Unexpected Exception in getInitialConditions.");
}
DataBlockWriter SBWstructural::getReactions(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getReactions();

	END_TRY_THROW_SBW("Unexpected Exception in getReactions.");
}
DataBlockWriter SBWstructural::getReactionsNamesList(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getReactionsNamesList();

	END_TRY_THROW_SBW("Unexpected Exception in getReactionsNamesList.");
}
DataBlockWriter SBWstructural::validateStructuralMatrices(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->validateStructuralMatrices();

	END_TRY_THROW_SBW("Unexpected Exception in validateStructuralMatrices.");
}
DataBlockWriter SBWstructural::getTestDetails(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->getTestDetails();

	END_TRY_THROW_SBW("Unexpected Exception in getTestDetails.");
}
DataBlockWriter SBWstructural::analyzeWithQR(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->analyzeWithQR();

	END_TRY_THROW_SBW("Unexpected Exception in analyzeWithQR.");
}
DataBlockWriter SBWstructural::analyzeWithLU(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->analyzeWithLU();

	END_TRY_THROW_SBW("Unexpected Exception in analyzeWithLU.");
}
DataBlockWriter SBWstructural::analyzeWithLUandRunTests(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->analyzeWithLUandRunTests();


	END_TRY_THROW_SBW("Unexpected Exception in analyzeWithLUandRunTests.");
}
DataBlockWriter SBWstructural::analyzeWithFullyPivotedLU(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->analyzeWithFullyPivotedLU();

	END_TRY_THROW_SBW("Unexpected Exception in analyzeWithFullyPivotedLU.");
}
DataBlockWriter SBWstructural::analyzeWithFullyPivotedLUwithTests(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	return DataBlockWriter() << _Instance ->analyzeWithFullyPivotedLUwithTests();

	END_TRY_THROW_SBW("Unexpected Exception in analyzeWithFullyPivotedLUwithTests.");
}
DataBlockWriter SBWstructural::analyzeWithGE(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;
	throw new SBWApplicationException("not implemented", "not implemented");
	END_TRY_THROW_SBW("Unexpected Exception in analyzeWithGE.");
}
DataBlockWriter SBWstructural::getReorderedStoichiometryMatrix(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	LibStructural::DoubleMatrix* oMatrix = _Instance->getReorderedStoichiometryMatrix();

	DataBlockWriter oWriter;   

	if (oMatrix == NULL) SBWutil::AddEmptyDoubleMatrix(oWriter);
	else SBWutil::AddToWriter(*oMatrix,oWriter); 

	return oWriter;

	END_TRY_THROW_SBW("Unexpected Exception in getReorderedStoichiometryMatrix.");
}
DataBlockWriter SBWstructural::getStoichiometryMatrix(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	LibStructural::DoubleMatrix* oMatrix = _Instance->getStoichiometryMatrix();

	DataBlockWriter oWriter;   

	if (oMatrix == NULL) SBWutil::AddEmptyDoubleMatrix(oWriter);
	else SBWutil::AddToWriter(*oMatrix,oWriter); 

	return oWriter;

	END_TRY_THROW_SBW("Unexpected Exception in getStoichiometryMatrix.");
}
DataBlockWriter SBWstructural::setTolerance(Module /*from*/, DataBlockReader reader)
{
	BEGIN_TRY;

	double dTolerance; reader >> dTolerance;
	_Instance->setTolerance(dTolerance);
	return DataBlockWriter();

	END_TRY_THROW_SBW("Unexpected Exception in setTolerance.");
}


SBWstructural::SBWstructural(void)
{
	_Instance = LibStructural::getInstance();
}

SBWstructural::~SBWstructural(void)
{
}
