####################################################################
# CMake Build Script for lpsolve
#
# Author: Frank T. Bergmann
# 

####################################################################
#
# Find all sources 
#
	
set(LP_SOURCES 
	lp_MDO.c shared/commonlib.c colamd/colamd.c	   
	shared/mmio.c shared/myblas.c ini.c fortify.c lp_rlp.c lp_crash.c  
	lp_Hash.c lp_lib.c lp_wlp.c lp_matrix.c lp_mipbb.c lp_MPS.c	   
	lp_params.c lp_presolve.c lp_price.c lp_pricePSE.c lp_report.c	   
	lp_scale.c lp_simplex.c lp_SOS.c lp_utils.c yacc_read.c
	bfp/bfp_LUSOL/lp_LUSOL.c
	bfp/bfp_LUSOL/LUSOL/lusol.c
	)

if (NOT UNIX)
	set(LP_SOURCES ${LP_SOURCES} bfp/bfp_LUSOL/bfp_LUSOL.c)
	add_definitions(	-DWIN32)
endif()
	
include_directories(${CMAKE_CURRENT_SOURCE_DIR})	
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/bfp)	
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/bfp/bfp_LUSOL)	
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/bfp/bfp_LUSOL/LUSOL)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/colamd)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/shared)	

add_definitions( 
    -DYY_NEVER_INTERACTIVE 
	-DPARSER_LP 
	-DINVERSE_ACTIVE=INVERSE_LUSOL 
	-DRoleIsExternalInvEngine
	-DLPSOLVE_STATIC
)

####################################################################
#
# Build library
#

#message(FATAL_ERROR 
#"""
#  Project: lpSolve
#
#  Static Runtime: ${WITH_STATIC_RUNTIME}
#  Build Type: ${CMAKE_BUILD_TYPE}
#  FLAGS: ${CMAKE_CXX_FLAGS}
#  FLAGS: ${CMAKE_CXX_FLAGS_RELEASE}
#  LDFLAGS: ${CMAKE_SHARED_LINKER_FLAGS}
#"""
#)

add_library (lpsolve-static STATIC ${LP_SOURCES} )

INSTALL(TARGETS lpsolve-static
	RUNTIME DESTINATION bin
	LIBRARY DESTINATION lib
	ARCHIVE DESTINATION lib
  )

