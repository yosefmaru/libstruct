####################################################################
#
# CMake Build Script for SBW LibStruct module
#
# Author: Frank T. Bergmann
# $Id$
# $HeadURL$


####################################################################
#
# Find all sources 
#
	
file(GLOB SBW_STRUCT_SOURCES 
	*.cpp 	
	../SBW_CLAPACK/sbwutil.cpp
	)

	
include_directories(${CMAKE_CURRENT_SOURCE_DIR})	
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../SBW_CLAPACK)

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

add_executable (SBW_Structural ${EXE_FLAGS} ${SBW_STRUCT_SOURCES} )
target_link_libraries(SBW_Structural ${LA_LIBS} LibStructural-static ${SBW_LIBRARY} ${EXTRA_LIBS})


INSTALL(TARGETS SBW_Structural
	RUNTIME DESTINATION bin
  )

