####################################################################
#
# CMake Build Script for SBW Clapack module
#
# Author: Frank T. Bergmann
# $Id$
# $HeadURL$


####################################################################
#
# Find all sources 
#
	
file(GLOB SBW_LAPACK_SOURCES 
	*.cpp 	
	)

	
include_directories(${CMAKE_CURRENT_SOURCE_DIR})	
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

####################################################################
#
# Build library
#

set(EXE_FLAGS)
if (MSVC OR USING_INTEL)
add_definitions(-DNO_API )
set(EXE_FLAGS WIN32)
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /ENTRY:mainCRTStartup")
endif(MSVC OR USING_INTEL)


add_executable (SBW_CLAPACK ${EXE_FLAGS} ${SBW_LAPACK_SOURCES} )
target_link_libraries(SBW_CLAPACK ${LA_LIBS} LibLA-static ${SBW_LIBRARY} ${EXTRA_LIBS})


INSTALL(TARGETS SBW_CLAPACK
	RUNTIME DESTINATION bin
  )

