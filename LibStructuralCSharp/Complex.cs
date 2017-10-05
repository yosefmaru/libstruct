// Author: fbergmann
// Project: LibStructuralCSharp
// Path: C:\Users\fbergmann\Documents\Visual Studio Codename Orcas\Projects\CLAPACK\LibStructuralCSharp
// Creation date: 6/27/2008 5:26 PM
// Last modified: 7/3/2008 12:10 PM

using System;

namespace libstructural
{
    /// <summary>
    /// Complex represents a complex number. (i.e: a number with real and imaginary part).
    /// </summary>
    public class Complex
    {
        private double _Real;
        /// <summary>
        /// Real part of the complex number
        /// </summary>
        public double Real
        {
            get { return _Real; } // get
            set { _Real = value; } // set
        } // Real

        private double _Imag;
        /// <summary>
        /// Imaginary part of the complex number
        /// </summary>
        public double Imag
        {
            get { return _Imag; } // get
            set { _Imag = value; } // set
        } // Imag

        /// <summary>
        /// Initializes a new complex number
        /// </summary>
        public Complex()
        {
            _Real = 0.0; _Imag = 0.0;
        } // Complex()

        /// <summary>
        /// Initializes a new complex number with given real and imaginary part
        /// </summary>
        /// <param name="real">real part</param>
        /// <param name="imag">imaginary part</param>
        public Complex(double real, double imag)
        {
            _Real = real;
            _Imag = imag;
        } // Complex(real, imag)


        /// <summary>
        /// Returns a string representation of the number as '(' + real + ' + ' + imag + 'i)'
        /// </summary>
        public override string ToString()
        {
            return "(" + _Real.ToString("G4") + " + " + _Imag.ToString("G4") + "i)";
        } // ToString()

        /// <summary>
        /// Override of Equals method, to make sure that two complex objects can be 
        /// compared. Two complex objects are seen as equal if their real and imaginary 
        /// parts are the same.
        /// </summary>
        /// <param name="obj">object to be compared to this instance</param>
        /// <returns>true, if real and imaginary parts match, false otherwise</returns>
        public override bool Equals(object obj)
        {
            if (obj is Complex)
            {
                Complex oTemp = (Complex)obj;
                return oTemp._Real == Real && oTemp.Imag == Imag;
            }
            return base.Equals(obj);
        }

        /// <summary>
        /// since we've overridden the equals method, we should override this one too
        /// </summary>
        /// <returns>the hash code for this object</returns>
        public override int GetHashCode()
        {
            return base.GetHashCode();
        }

        
        /// <summary>
        /// Addition of two complex numbers
        /// </summary>
        public static Complex operator +(Complex a, Complex b)
        {
            return new Complex(a._Real + b._Real, a._Imag + b._Imag);
        }

        /// <summary>
        /// Substraction of two complex numbers
        /// </summary>
        public static Complex operator -(Complex a, Complex b)
        {
            return new Complex(a._Real - b._Real, a._Imag - b._Imag);
        }

        /// <summary>
        /// Substraction of two complex numbers
        /// </summary>
        public static Complex[] SubtractArrays(Complex[] a, Complex[] b)
        {
            Complex[] result = new Complex[a.Length];
            for (int i = 0; i < a.Length; i++)
            {
                result[i] = a[i] - b[i];
            }
            return result;
        }

        /// <summary>
        /// Multiplication of two complex numbers
        /// </summary>
        public static Complex operator *(Complex a, Complex b)
        {
            return (new Complex(a._Real * b._Real - a._Imag * b._Imag,
            a._Real * b._Imag + b._Real * a._Imag));
        }

        public static Complex ComplexConjugate(Complex a)
        {
            return new Complex(a._Real, -a._Imag);
        }
        public Complex ComplexConjugate()
        {
            return new Complex(_Real, -Imag);
        }

        /// <summary>
        /// Multiplication of complex number with scalar
        /// </summary>
        public static Complex operator *(Complex a, double b)
        {
            return (new Complex(a._Real * b, a._Imag*b));
        }

        /// <summary>
        /// Division of complex number with scalar
        /// </summary>
        public static Complex operator /(Complex a, double b)
        {
            return (new Complex(a._Real / b, a._Imag / b));
        }

                /// <summary>
        /// Multiplication of complex number with scalar
        /// </summary>
        public static Complex operator *(double b,Complex a)
        {
            return (new Complex(a._Real * b, a._Imag*b));
        }

        /// <summary>
        /// Division of complex number with scalar
        /// </summary>
        public static Complex operator /(double b,Complex a)
        {
            return (new Complex(a._Real / b, a._Imag / b));
        }


        /// <summary>
        /// Division of two complex numbers
        /// </summary>
        public static Complex operator /(Complex a, Complex b)
        {
            if ((b._Real == 0.0f) &&
            (b._Imag == 0.0f))
                throw new DivideByZeroException("Can't divide by zero Complex number");

            double newReal =
            (a._Real * b._Real + a._Imag * b._Imag) /
            (b._Real * b._Real + b._Imag * b._Imag);
            double newImaginary =
            (b._Real * a._Imag - a._Real * b._Imag) /
            (b._Real * b._Real + b._Imag * b._Imag);

            return (new Complex(newReal, newImaginary));
        }

        ///// <summary>
        ///// Implicit conversion returns real part
        ///// </summary>
        //public static implicit operator double (Complex a)
        //{
        //    return a._Real;
        //}

        ///// <summary>
        ///// Implicit conversion contructs new complex number with 0 imaginary part
        ///// </summary>
        //public static implicit operator Complex(double a)
        //{
        //    return new Complex(a, 0);
        //}
        

    } // class Complex
} // namespace libstructural
