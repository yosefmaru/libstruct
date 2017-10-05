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
    /// QRResult is intended to hold the return values of the Clapack QR factorization methods (
    /// <see cref="libstructural.LA.GetQRWithPivot"/> and <see cref="libstructural.LA.GetQR"/>).
    /// </summary>
    public class QRResult
    {
        private double[][] _Q;
        /// <summary>
        /// The Q Matrix is an orthogonal matrix. 
        /// </summary>
        public double[][] Q
        {
            get { return _Q; } // get
            set { _Q = value; } // set
        } // Q

        private double[][] _R;
        /// <summary>
        /// The R Matrix is an upper triangular matrix
        /// </summary>
        public double[][] R
        {
            get { return _R; } // get
            set { _R = value; } // set
        } // R

        private double[][] _P;
        /// <summary>
        /// P is a permutation matrix, only available after a call to 
        /// <see cref="libstructural.LA.GetQRWithPivot"/>.
        /// </summary>
        public double[][] P
        {
            get { return _P; } // get
            set { _P = value; } // set
        } // P

        /// <summary>
        /// Create a new QR result class with double matrices Q, R and P
        /// </summary>
        /// <param name="q">Q matrix</param>
        /// <param name="r">R matrix</param>
        /// <param name="p">P matrix</param>
        public QRResult(double[][] q, double[][] r, double[][] p)
        {
            _Q = q;
            _R = r;
            _P = p;
        } // QRResult(q, r, p)

        /// <summary>
        /// Create a new QR result class with double matrices Q, R
        /// </summary>
        /// <param name="q">Q matrix</param>
        /// <param name="r">R matrix</param>
        public QRResult(double[][] q, double[][] r)
        {
            _Q = q;
            _R = r;
        } // QRResult(q, r)

    } // class QRResult

} // namespace libstructural
