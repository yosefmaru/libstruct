// Author: fbergmann
// Project: LibStructuralCSharp
// Path: C:\Users\fbergmann\Documents\Visual Studio Codename Orcas\Projects\CLAPACK\LibStructuralCSharp
// Creation date: 6/27/2008 5:26 PM
// Last modified: 7/3/2008 12:10 PM

#region Using directives
using System;
using System.Runtime.InteropServices;
#endregion

namespace libstructural
{
    /// <summary>
    /// LUResult is intended to hold the return values of the Clapack LU decomposition methods (
    /// <see cref="libstructural.LA.GetLUWithPivoting"/> and <see cref="libstructural.LA.GetLU"/>).
    /// </summary>
    public class LUResult
    {
        private int _Info;
        /// <summary>
        /// <para>Info represents status information about the LU factorization its value is to be interpreted as: </para>
        /// <ul>
        /// <li>0:  successful exit</li>
        /// <li> &lt; 0:  if INFO = -i, the i-th argument had an illegal value</li>
        /// <li> &gt; 0:  if INFO = i, U(i,i) is exactly zero. The factorization
        /// has been completed, but the factor U is exactly
        /// singular, and division by zero will occur if it is used
        /// to solve a system of equations.</li>
        /// </ul>
        /// 
        /// </summary>
        public int Info
        {
            get { return _Info; } // get
            set { _Info = value; } // set
        } // Info

        private double[][] _L;
        /// <summary>
        /// L is a lower triangular matrix
        /// </summary>
        public double[][] L
        {
            get { return _L; } // get
            set { _L = value; } // set
        } // L

        private double[][] _U;
        /// <summary>
        /// U is an upper triangular matrix
        /// </summary>
        public double[][] U
        {
            get { return _U; } // get
            set { _U = value; } // set
        } // U

        private int[][] _P;
        /// <summary>
        /// P is a permutation matrix representing row permutations
        /// </summary>
        public int[][] P
        {
            get { return _P; } // get
            set { _P = value; } // set
        } // P

        private int[][] _Q;
        /// <summary>
        /// Q is a permutation matrix representing column permutations and is
        /// only available after a call to <see cref="libstructural.LA.GetLUWithPivoting"/> 
        /// and null otherwise
        /// </summary>
        public int[][] Q
        {
            get { return _Q; } // get
            set { _Q = value; } // set
        } // Q

        /// <summary>
        /// Creates a new LUResult with the given matrices and info flag
        /// </summary>
        /// <param name="info">the information flag, see <see cref="libstructural.LUResult.Info"/></param>
        /// <param name="l">the L matrix, see <see cref="libstructural.LUResult.L"/></param>
        /// <param name="u">the U matrix, see <see cref="libstructural.LUResult.U"/></param>
        /// <param name="p">the P matrix, see <see cref="libstructural.LUResult.P"/></param>
        /// <param name="q">the Q matrix, see <see cref="libstructural.LUResult.Q"/></param>
        public LUResult(int info, double[][] l, double[][] u, int[][] p, int[][] q)
        {
            _Info = info;
            _L = l;
            _U = u;
            _P = p;
            _Q = q;
        } // LUResult(info, l, u)

        /// <summary>
        /// Creates a new LUResult with the given matrices and info flag
        /// </summary>
        /// <param name="info">the information flag, see <see cref="libstructural.LUResult.Info"/></param>
        /// <param name="l">the L matrix, see <see cref="libstructural.LUResult.L"/></param>
        /// <param name="u">the U matrix, see <see cref="libstructural.LUResult.U"/></param>
        /// <param name="p">the P matrix, see <see cref="libstructural.LUResult.P"/></param>
        public LUResult(int info, double[][] l, double[][] u, int[][] p)
        {
            _Info = info;
            _L = l;
            _U = u;
            _P = p;
        
        } // LUResult(info, l, u)
    } // class LUResult
} // namespace libstructural
