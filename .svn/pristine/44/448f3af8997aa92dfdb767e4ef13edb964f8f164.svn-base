using System;
using System.Collections.Generic;
using System.Text;
using System.Runtime.InteropServices;

namespace libstructural
{
    /// <summary>
    /// An Enum containing supported flux balance operations, as used by
    /// addConstraint
    /// </summary>
    public enum FluxBalanceOperation
    {
        /// <summary>
        /// The constraint has to be less or equal to the given value
        /// </summary>
        LE = 1,
        /// <summary>
        /// The constraint has to be greater or equal to the given value
        /// </summary>
        GE = 2,
        /// <summary>
        /// The constrint has to equal to the given value
        /// </summary>
        EQ = 3
    }


    /// <summary>
    /// Enum specifying the export types supported in writeToFile.
    /// </summary>
    public enum ExportTypes
    {
        /// <summary>
        /// Export the loaded model as LP file
        /// </summary>
        LP,
        /// <summary>
        /// Export the loaded model as MPS file
        /// </summary>
        MPS,
        /// <summary>
        /// Export the loaded model as FreeMPS file
        /// </summary>
        FreeMPS    
    }

    /// <summary>
    /// First implementation of a Flux Balance analysis class based on LPsolve. 
    /// The actual routines have been embedded in LibStruct, and here only the 
    /// wrapped methods are called. 
    /// </summary>
    public static class FluxBalance
    {
        /// <summary>
        /// The library file to where the members will be found. This will be 
        /// libstructural.dll on windows, and libLibStructural.so on linux and 
        /// OSX under mono.
        /// </summary>
        internal const string LIBRARY_FILE = "LibStructural";


        /// <summary>
        /// Loads a new SBML model into the LPsolve Library 
        /// </summary>
        /// <param name="sbmlContent"></param>
        public static void LoadSBML(string sbmlContent)
        {
            FluxBalance_loadSBML(sbmlContent);
        }

        /// <summary>
        /// Loads the given stoichiometry matrix into the flux balance class, 
        /// as well as the given array of fluxNames. Note that the number of columns
        /// of the stoichiometry matrix and the number of elements in the fluxNames
        /// array have to match. 
        /// </summary>
        /// <param name="matrix">stoichiometry matrix to load</param>
        /// <param name="fluxNames">fluxnames corresponding to the columns of 
        /// the stoichiometry matrix</param>
        public static void LoadStoichiometry(double[][] matrix, string[] fluxNames)
        {            
            IntPtr pointer; int nRows; int nCols;
            InteropUtil.MapMatrixToPointer(matrix, out pointer, out nRows, out nCols);

            IntPtr ptrNames; int nLength;
            InteropUtil.MapStringArrayToPointer(fluxNames, out ptrNames, out nLength);

            FluxBalance_loadStoichiometry(pointer, nRows, nCols, ptrNames);

            InteropUtil.FreePtrMatrix(pointer, nRows);
            InteropUtil.FreePtrMatrix(ptrNames, nLength);
        }

        /// <summary>
        /// Clears all Contraints currently set
        /// </summary>
        public static void ClearConstraints()
        {
            FluxBalance_clearConstraints();
        }

        /// <summary>
        /// Clears all Objectives currently set
        /// </summary>
        public static void ClearObjectives()
        {
            FluxBalance_clearObjectives();
        }

        /// <summary>
        /// Adds a new Linear constraint. 
        /// </summary>
        /// <param name="id">flux id of the contraint</param>
        /// <param name="operation">Type of operation, =, &gt;= or &lt;= </param>
        /// <param name="value">the constraint value</param>
        public static void AddConstraint(string id, FluxBalanceOperation operation, double value)
        {
            FluxBalance_addConstraint(id, (int)operation, value);
        }

        /// <summary>
        /// Adds a new objective to be targetet by the maximization. 
        /// </summary>
        /// <param name="id">flux it of the objective</param>
        /// <param name="value">target value</param>
        public static void AddObjective(string id, double value)
        {
            FluxBalance_addObjective(id, value);
        }

        /// <summary>
        /// Replaces current Constraints with those provided in the arrays. Note that
        /// all arrays should have the same length. 
        /// </summary>
        /// <param name="ids">array of flux ids</param>
        /// <param name="operations">array of FluxBalanceOperations</param>
        /// <param name="values">array of constraint values</param>
        public static void SetConstraints(string[] ids, FluxBalanceOperation[] operations, double[] values)
        {
            IntPtr ptrReactionNames; int nLength;
            InteropUtil.MapStringArrayToPointer(ids, out ptrReactionNames, out nLength);

            int[] intOperations = new int[operations.Length];
            for (int i = 0; i < operations.Length; i++)
            {
                intOperations[i] = (int)operations[i];
            }

            IntPtr ptrOpValues;
            InteropUtil.MapIntArrayToPointer(intOperations, out ptrOpValues, out nLength);

            IntPtr ptrValues;
            InteropUtil.MapDoubleArrayToPointer(values, out ptrValues, out nLength);

            FluxBalance_setConstraints(ptrReactionNames, ptrOpValues, ptrValues, nLength);

            InteropUtil.FreePtrMatrix(ptrReactionNames, nLength);
            InteropUtil.FreePtrVector(ptrOpValues);
            InteropUtil.FreePtrVector(ptrValues);
        }

        /// <summary>
        /// Replaces current objective function values with the ones provided in the arrays.
        /// </summary>
        /// <param name="ids">array of flux ids</param>
        /// <param name="values">corresponding coefficients</param>
        public static void SetObjectives(string[] ids, double[] values)
        {
            IntPtr ptrReactionNames; int nLength;
            InteropUtil.MapStringArrayToPointer(ids, out ptrReactionNames, out nLength);


            IntPtr ptrValues;
            InteropUtil.MapDoubleArrayToPointer(values, out ptrValues, out nLength);

            FluxBalance_setObjectives(ptrReactionNames, ptrValues, nLength);

            InteropUtil.FreePtrMatrix(ptrReactionNames, nLength);
            InteropUtil.FreePtrVector(ptrValues);
        }

        /// <summary>
        /// Solves the Flux Balance maximization. And returns the result. 
        /// </summary>
        /// <param name="names">flux id's corresponding to the values</param>
        /// <returns>the values</returns>
        public static double[] Solve(out string[] names)
        {
            IntPtr outVariableNames; IntPtr outValues; int outLength;
            FluxBalance_solve(out outVariableNames, out outValues, out outLength);

            names = InteropUtil.GetStringArrayFromPtr(outVariableNames, outLength);
            return InteropUtil.GetDoubleArrayFromPtr(outValues, outLength);
        }

        /// <summary>
        /// Solves the Flux Balance maximization. And returns the result. 
        /// </summary>
        /// <param name="names">flux id's corresponding to the values</param>
        /// <returns>the values</returns>
        public static double[] Maximize(out string[] names)
        {
            IntPtr outVariableNames; IntPtr outValues; int outLength;
            FluxBalance_maximize(out outVariableNames, out outValues, out outLength);

            names = InteropUtil.GetStringArrayFromPtr(outVariableNames, outLength);
            return InteropUtil.GetDoubleArrayFromPtr(outValues, outLength);
        }

        /// <summary>
        /// Solves the Flux Balance minimization. And returns the result. 
        /// </summary>
        /// <param name="names">flux id's corresponding to the values</param>
        /// <returns>the values</returns>
        public static double[] Minimize(out string[] names)
        {
            IntPtr outVariableNames; IntPtr outValues; int outLength;
            FluxBalance_minimize(out outVariableNames, out outValues, out outLength);

            names = InteropUtil.GetStringArrayFromPtr(outVariableNames, outLength);
            return InteropUtil.GetDoubleArrayFromPtr(outValues, outLength);
        }

        /// <summary>
        /// Writes out the current constraints, objective function as LP file
        /// </summary>
        /// <param name="fileName">fileName to write the LP file to.</param>
        public static void WriteToFile(string fileName)
        {
            WriteToFile(fileName, ExportTypes.LP);
        }
        /// <summary>
        /// Writes out the current constraints, objective function as LP, MPS, 
        /// freeMPS or XLI file.
        /// </summary>
        /// <param name="fileName">fileName to write to.</param>
        /// <param name="format">The format the file should be exported as.</param>
        public static void WriteToFile(string fileName, ExportTypes format)
        {
            switch (format)
            {
                case ExportTypes.LP:
                    FluxBalance_writeToLPFile(fileName);
                    break;
                case ExportTypes.MPS:
                    FluxBalance_writeToMPSFile(fileName);
                    break;
                case ExportTypes.FreeMPS:
                    FluxBalance_writeToFreeMPSFile(fileName);
                    break;
                default:
                    break;
            }            
        }

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_loadSBML")]
        internal static extern int FluxBalance_loadSBML(string sbmlContent);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_loadStoichiometry")]
        internal static extern int FluxBalance_loadStoichiometry(IntPtr oMatrix, int nRows, int nCols, IntPtr fluxNames);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_clearConstraints")]
        internal static extern int FluxBalance_clearConstraints();

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_addConstraint")]
        internal static extern int FluxBalance_addConstraint(string id, int operation, double value);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_setConstraints")]
        internal static extern int FluxBalance_setConstraints(IntPtr ids, IntPtr operations, IntPtr values, int length);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_clearObjectives")]
        internal static extern int FluxBalance_clearObjectives();

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_addObjective")]
        internal static extern int FluxBalance_addObjective(string id, double value);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_setObjectives")]
        internal static extern int FluxBalance_setObjectives(IntPtr ids, IntPtr values, int length);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_solve")]
        internal static extern int FluxBalance_solve(out IntPtr outNames, out IntPtr outValues, out int outLength);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_minimize")]
        internal static extern int FluxBalance_minimize(out IntPtr outNames, out IntPtr outValues, out int outLength);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_maximize")]
        internal static extern int FluxBalance_maximize(out IntPtr outNames, out IntPtr outValues, out int outLength);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_writeToLPFile")]
        internal static extern int FluxBalance_writeToLPFile(string fileName);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_writeToMPSFile")]
        internal static extern int FluxBalance_writeToMPSFile(string fileName);

        [DllImportAttribute(LIBRARY_FILE, EntryPoint = "FluxBalance_writeToFreeMPSFile")]
        internal static extern int FluxBalance_writeToFreeMPSFile(string fileName);

    }
}
