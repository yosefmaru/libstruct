#include "sbwclapack.h"
#include <SBW/ModuleImpl.h>

#define SC_NAME         "SBW_CLAPACK"
#define SC_VERSION      "2.00"
#define SC_AUTHOR       "Ravishankar Rao Vallabhajosyula"
#define SC_DESCRIPTION  "SBW Interface to CLAPACK for Numerical Analysis"
#define SC_DISPLAYNAME  "SBW_CLAPACK"
#define SC_COPYRIGHT    "BSD"
#define SC_URL          "www.sys-bio.org"

int main(int argc, char* argv[])
{
	try
	{
		ModuleImpl modImpl(
		   "edu.kgi.SBW_CLAPACK",		// module identification
		   "Access to LAPACK from SBW", // humanly readable name
		   UniqueModule,				// management scheme
		   SC_DESCRIPTION				// help string
		   ); 

		modImpl.addServiceObject(
		   SC_NAME,							// service identification
		   SC_DISPLAYNAME,					// humanly readable name
		   "",								// category
		   new SBW_CLAPACK::SBWclapack(),	// service implementation
		   SC_DESCRIPTION					// help string
		   ); 

		// connect to broker providing services
		modImpl.run(argc, argv);
		return 0;
	}
	catch (SBWException *e)
	{
		fprintf(stderr, "SBW CLAPACK exception: %s\n", e->getMessage().c_str());
		return -1;
	}
	catch (...) 
	{
		fprintf(stderr,	"Unknown SBW CLAPACK Exception. \n");
		return -1;
	}
	return 0;
}

