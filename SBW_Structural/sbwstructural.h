#ifndef SBW_STRUCTURAL_CONSERVATION_H
#define SBW_STRUCTURAL_CONSERVATION_H

#include <SBW/Module.h>
#include <SBW/MethodTable.h>
#include <SBW/DataBlockReader.h>
#include <SBW/DataBlockWriter.h>


#define CONSV_NAME         "edu.kgi.StructAnalysis"
#define CONSV_SERVICENAME  "StructAnalysis"
#define CONSV_VERSION      "2.0"
#define CONSV_AUTHOR       "Frank Bergmann and Ravishankar Rao Vallabhajosyula"
#define CONSV_DESCRIPTION  "Structural Analysis for Biochemical Networks"
#define CONSV_DISPLAYNAME  "Structural Analysis Module"
#define CONSV_COPYRIGHT    "(c) 2005-2008 SBW Team"
#define CONSV_URL          "www.sys-bio.org"

#include "libstructural.h"

namespace SBW_STRUCTURAL
{

	class SBWstructural
	{
	public: 

		SystemsBiologyWorkbench::DataBlockWriter getName(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getVersion(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getAuthor(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getDescription(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getDisplayName(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getCopyright(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getURL(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);

#ifndef NO_SBML
		SystemsBiologyWorkbench::DataBlockWriter loadSBML(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter loadSBMLwithTests(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
#endif

		SystemsBiologyWorkbench::DataBlockWriter getL0Matrix(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getNrMatrix(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getN0Matrix(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getK0Matrix(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getLinkMatrix(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getKMatrix(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getModelName(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getNumSpecies(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getNumIndSpecies(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getNumDepSpecies(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getNumReactions(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getRank(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getNmatrixSparsity(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getGammaMatrix(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getConservedSums(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getConservedLaws(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);

		SystemsBiologyWorkbench::DataBlockWriter getReorderedSpecies(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getReorderedSpeciesNamesList(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getIndependentSpecies(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getIndependentSpeciesNamesList(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getDependentSpecies(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getDependentSpeciesNamesList(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getInitialConditions(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getReactions(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getReactionsNamesList(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter validateStructuralMatrices(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);

		SystemsBiologyWorkbench::DataBlockWriter getTestDetails(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);

		SystemsBiologyWorkbench::DataBlockWriter analyzeWithQR(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter analyzeWithLU(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter analyzeWithLUandRunTests(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter analyzeWithFullyPivotedLU(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter analyzeWithFullyPivotedLUwithTests(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter analyzeWithGE(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);

		SystemsBiologyWorkbench::DataBlockWriter getReorderedStoichiometryMatrix(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);
		SystemsBiologyWorkbench::DataBlockWriter getStoichiometryMatrix(SystemsBiologyWorkbench::Module from, SystemsBiologyWorkbench::DataBlockReader reader);

		DataBlockWriter setTolerance(Module from, DataBlockReader reader);

		static void registerMethods(SystemsBiologyWorkbench::MethodTable<SBWstructural> &table)
		{
#ifndef NO_SBML
			table.addMethod(&SBWstructural::loadSBML,                                "string loadSBML(string)",                       true, "Initialization method, takes SBML as input");
			table.addMethod(&SBWstructural::loadSBMLwithTests,                       "string loadSBMLwithTests(string)",              true, "Initialization method, takes SBML as input");
#endif
			table.addMethod(&SBWstructural::analyzeWithLU,                           "string analyzeWithLU()",                       false, "Uses LU Decomposition for Conservation analysis");
			table.addMethod(&SBWstructural::analyzeWithLUandRunTests,                "string analyzeWithLUandRunTests()",            false, "Uses LU Decomposition for Conservation analysis");
			table.addMethod(&SBWstructural::analyzeWithFullyPivotedLU,               "string analyzeWithFullyPivotedLU()",           false, "Uses fully pivoted LU Decomposition for Conservation analysis");
			table.addMethod(&SBWstructural::analyzeWithFullyPivotedLUwithTests,      "string analyzeWithFullyPivotedLUwithTests()",  false, "Uses fully pivoted LU Decomposition for Conservation analysis");
			table.addMethod(&SBWstructural::getL0Matrix,                             "double[][] getL0Matrix()",                     false, "Returns L0 Matrix");
			table.addMethod(&SBWstructural::getNrMatrix,                             "double[][] getNrMatrix()",                     false, "Returns Nr Matrix");
			table.addMethod(&SBWstructural::getN0Matrix,                             "double[][] getN0Matrix()",                     false, "Returns N0 Matrix");
			table.addMethod(&SBWstructural::getLinkMatrix,                           "double[][] getLinkMatrix()",                   false, "Returns L, the Link Matrix");
			table.addMethod(&SBWstructural::getK0Matrix,                             "double[][] getK0Matrix()",                     false, "Returns K0 Matrix ");
			table.addMethod(&SBWstructural::getKMatrix,                              "double[][] getNullSpace()",                    false, "Returns the K Matrix (Nullspace");
			table.addMethod(&SBWstructural::getReorderedSpecies,                     "string[] getReorderedSpecies()",               false, "Returns the reordered list of species ");
			table.addMethod(&SBWstructural::getReorderedSpeciesNamesList,            "string[] getReorderedSpeciesNamesList()",      false, "Returns the actual names of the reordered species ");
			table.addMethod(&SBWstructural::getIndependentSpecies,                   "string[] getIndependentSpecies()",             false, "Returns the list of independent species ");
			table.addMethod(&SBWstructural::getIndependentSpeciesNamesList,          "string[] getIndependentSpeciesNamesList()",    false, "Returns the actual names of the independent species ");
			table.addMethod(&SBWstructural::getDependentSpecies,                     "string[] getDependentSpecies()",               false, "Returns the list of dependent species ");
			table.addMethod(&SBWstructural::getDependentSpeciesNamesList,            "string[] getDependentSpeciesNamesList()",      false, "Returns the actual names of the dependent species ");
			table.addMethod(&SBWstructural::getReactions,                            "string[] getReactions()",                      false, "Returns the list of Reactions ");
			table.addMethod(&SBWstructural::getReactionsNamesList,                   "string[] getReactionsNamesList()",             false, "Returns actual names of the Reactions ");
			table.addMethod(&SBWstructural::getGammaMatrix,                          "double[][] getConservationLawArray()",         false, "Returns Gamma, the conservation law array ");
			table.addMethod(&SBWstructural::getConservedLaws,                        "string[] getConservedEntities()",              false, "Returns algebraic expressions for conserved cycles ");
			table.addMethod(&SBWstructural::getConservedSums,                        "double[] getConservedSums()",                  false, "Returns values for conserved cycles using Initial conditions ");
			table.addMethod(&SBWstructural::getInitialConditions,                    "{} getInitialConditions()",                    false, "Returns Initial Conditions used in the model");
			table.addMethod(&SBWstructural::getStoichiometryMatrix,                  "double[][] getStoichiometryMatrix()",          false, "Returns the original stoichiometry matrix");
			table.addMethod(&SBWstructural::getReorderedStoichiometryMatrix,         "double[][] getReorderedStoichiometryMatrix()", false, "Returns reordered stoichiometry matrix");
			table.addMethod(&SBWstructural::validateStructuralMatrices,              "string[] testConservationLaws()",              false, "Tests if structural matrices are correct");
			table.addMethod(&SBWstructural::getTestDetails,                          "string getTestDetails()",                      false, "Return Details about structural tests");
			table.addMethod(&SBWstructural::getModelName,                            "string getModelName()",                        false, "Returns the name of the model");
			table.addMethod(&SBWstructural::getNumSpecies,                           "int getNumSpecies()",                          false, "Returns the total number of species");
			table.addMethod(&SBWstructural::getNumIndSpecies,                        "int getNumIndSpecies()",                       false, "Returns the number of independent species");
			table.addMethod(&SBWstructural::getNumDepSpecies,                        "int getNumDepSpecies()",                       false, "Returns the number of dependent species");
			table.addMethod(&SBWstructural::getNumReactions,                         "int getNumReactions()",                        false, "Returns the total number of reactions");
			table.addMethod(&SBWstructural::getRank,                                 "int getRank()",                                false, "Returns rank of stoichiometry matrix");
			table.addMethod(&SBWstructural::getNmatrixSparsity,                      "double getNmatrixSparsity()",                  false, "Returns the number of nonzero values in Stoichiometry matrix");
			table.addMethod(&SBWstructural::setTolerance,                            "void setTolerance(double)",                    false, "Set user specified tolerance");
			table.addMethod(&SBWstructural::getName,                                 "string getName()",                             false, CONSV_NAME);
			table.addMethod(&SBWstructural::getVersion,                              "string getVersion()",                          false, CONSV_VERSION);
			table.addMethod(&SBWstructural::getAuthor,                               "string getAuthor()",                           false, CONSV_AUTHOR);
			table.addMethod(&SBWstructural::getDescription,                          "string getDescription()",                      false, CONSV_DESCRIPTION);
			table.addMethod(&SBWstructural::getDisplayName,                          "string getDisplayName()",                      false, CONSV_DISPLAYNAME);
			table.addMethod(&SBWstructural::getCopyright,                            "string getCopyright()",                        false, CONSV_COPYRIGHT);
			table.addMethod(&SBWstructural::getURL,                                  "string getURL()",                              false, CONSV_URL);
		}


	public:
		SBWstructural(void);
		~SBWstructural(void);
	private:
		LIB_STRUCTURAL::LibStructural* _Instance;
	};

}

#endif // SBW_STRUCTURAL_CONSERVATION_H

