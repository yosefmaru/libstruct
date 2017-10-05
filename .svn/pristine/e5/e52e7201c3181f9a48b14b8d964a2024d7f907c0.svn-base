#include "sbwstructural.h"

#include <SBW/ModuleImpl.h>

using namespace SBW_STRUCTURAL;


int main(int argc, char* argv[])
{
	try
	{
		//StructAnalysis* SA = new StructAnalysis();
		//SA->first_run = true;
		//SA->zero_nmat_prev = false;

		ModuleImpl modImpl(
			CONSV_NAME,			// module identification
			CONSV_DISPLAYNAME,	// humanly readable name
			UniqueModule,		// management scheme
			CONSV_DESCRIPTION	// help string
			); 


		modImpl.addServiceObject(
			CONSV_SERVICENAME,		// service identification
			CONSV_DISPLAYNAME,		// humanly readable name
			"plugin",				// category
			new SBWstructural(),	// service implementation 
			CONSV_DESCRIPTION		// help string
			); 
			//new StructAnalysis()); // service implementation

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
}
