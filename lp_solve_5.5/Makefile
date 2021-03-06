PACKAGE_NAME=lpsolve
PACKAGE_STRING=lpsolve_5.5.0.14
CCSHARED=
prefix = /usr/local
includedir = ${prefix}/include/lpsolve
libdir = ${exec_prefix}/lib
CFLAGS=-arch ppc -arch i386
INCLUDES=-I. -I./shared -I./bfp -I./bfp/bfp_LUSOL -I./bfp/bfp_LUSOL/LUSOL -I./colamd
DEFINES=-DYY_NEVER_INTERACTIVE -DPARSER_LP -DINVERSE_ACTIVE=INVERSE_LUSOL -DRoleIsExternalInvEngine 
LIBS=-lc -lm -ldl
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_PROGRAM = ${INSTALL}
INSTALL_SCRIPT = ${INSTALL}
INSTALL = /usr/bin/install -c
mkdir_p = mkdir -p
HEADERS = \
	declare.h \
	fortify.h \
	ini.h	\
	lp_crash.h \
	lp_explicit.h \
	lp_fortify.h \
	lp_Hash.h \
	lpkit.h \
	lp_lib.h \
	lp_matrix.h \
	lp_MDO.h \
	lp_mipbb.h \
	lp_MPS.h \
	lp_presolve.h \
	lp_price.h \
	lp_pricePSE.h \
	lp_report.h \
	lp_rlp.h \
	lp_scale.h \
	lp_simplex.h \
	lp_solveDLL.h \
	lpsolve.h \
	lp_SOS.h \
	lp_types.h \
	lp_utils.h \
	lp_wlp.h \
	ufortify.h \
	yacc_read.h

SOURCES = lp_MDO.c \
	shared/commonlib.c \
	shared/mmio.c \
	shared/myblas.c \
	ini.c \
	fortify.c \
	colamd/colamd.c \
	lp_rlp.c \
	lp_crash.c \
	bfp/bfp_LUSOL/lp_LUSOL.c \
	bfp/bfp_LUSOL/LUSOL/lusol.c \
	lp_Hash.c \
	lp_lib.c \
	lp_wlp.c \
	lp_matrix.c \
	lp_mipbb.c \
	lp_MPS.c \
	lp_params.c \
	lp_presolve.c \
	lp_price.c \
	lp_pricePSE.c \
	lp_report.c \
	lp_scale.c \
	lp_simplex.c \
	lp_SOS.c \
	lp_utils.c \
        yacc_read.c

all: liblpsolve55.a liblpsolve55.so

# OBJECTS = $(patsubst %.c,%.o,$(SOURCES))
#.c.o:
#	$(CC) -s -c $(INCLUDES) $(CFLAGS) $(DEFINES) $(SOURCES)

liblpsolve55.a: $(SOURCES)
	$(CC) -s -c $(INCLUDES) $(CFLAGS) $(DEFINES) $(SOURCES)
	ar rv $@ `echo $(SOURCES)|sed s/[.]c/.o/g|sed 's/[^ ]*\///g'`
	ranlib $@

liblpsolve55.so: $(SOURCES)
	$(CC) $(CCSHARED) -s -c $(INCLUDES) $(CFLAGS) $(DEFINES) $(SOURCES)
	$(CC) -shared -Wl,-Bsymbolic -Wl,-soname,$@ -o $@ `echo $(SOURCES)|sed s/[.]c/.o/g|sed 's/[^ ]*\///g'` $(LIBS)

install: install-HEADERS install-LIBRARIES

install-HEADERS: $(HEADERS)
	test -d $(includedir) || $(mkdir_p) $(includedir)
	@list='$(HEADERS)'; for p in $$list; do \
	  echo " $(INSTALL) $$p $(includedir)/$$f"; \
	  $(INSTALL) $$p $(includedir)/$$f; \
	done

install-LIBRARIES: liblpsolve55.a liblpsolve55.so
	test -d $(libdir) || $(mkdir_p) $(libdir)
	@list='liblpsolve55.a liblpsolve55.so'; for p in $$list; do \
	  if test -f $$p; then \
	    echo " $(INSTALL) $$p $(libdir)/$$f"; \
	    $(INSTALL) $$p $(libdir)/$$f; \
	  else :; fi; \
	done

uninstall-LIBRARIES:
	@set -x; list='liblpsolve55.a liblpsolve55.so'; for p in $$list; do \
	  echo " rm -f $(libdir)/$$f"; \
	  rm -f "$(libdir)/$$f"; \
	done

uninstall: uninstall-HEADERS uninstall-LIBRARIES

uninstall-HEADERS:
	@set -x; @list=$(HEADERS); for p in $$list; do \
	  echo " rm -f $(includedir)/$$f"; \
	  rm -f "$(includedir)/$$f"; \
	done

dist: 
	mkdir $(PACKAGE_STRING)
	tar -cpf- -T MANIFEST | (cd  $(PACKAGE_STRING) && tar -xpf- )
	tar -czpf $(PACKAGE_STRING).tar.bz2 ./$(PACKAGE_STRING)
	-rm -fr $(PACKAGE_STRING)

CLEANFILES = *.o *.so *.a
clean:
	-rm -f $(CLEANFILES)

.PHONY: install install-HEADERS install-LIBRARIES uninstall uninstall-HEADERS uninstall-LIBRARIES all
