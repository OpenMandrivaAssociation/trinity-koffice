%bcond clang 1
%bcond kross 1
%bcond ruby 1
%bcond python 0
%bcond graphicsmagick 1
%bcond postresql 1
%bcond wv2 0

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg koffice
%define tde_prefix /opt/trinity


# Ruby 1.9 includes are located in strance directories ... (taken from ruby 1.9 spec file)
%global	_normalized_cpu	%(echo %{_target_cpu} | sed 's/^ppc/powerpc/;s/i.86/i386/;s/sparcv./sparc/;s/armv.*/arm/')

%global _disable_ld_no_undefined 1
%global build_cxxflags %optflags -Wl,--allow-shlib-undefined
%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.6.3
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	An integrated office suite
Group:		Applications/Productivity
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/office/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:	trinity-koffice-rpmlintrc

# BuildRequires: world-devel ;)
BuildRequires:  make
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tdegraphics-devel >= %{tde_version}
BuildRequires:	trinity-libpoppler-tqt-devel >= %{tde_version}

BuildRequires:	autoconf automake libtool m4

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(mariadb)
BuildRequires:	perl
BuildRequires:	doxygen
BuildRequires:	aspell-devel
BuildRequires:	pkgconfig(readline)

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# EXIF support
BuildRequires:  pkgconfig(libexif)

# IMAGEMAGICK support
BuildRequires:  pkgconfig(ImageMagick)

# JPEG support
BuildRequires:  pkgconfig(libjpeg)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# OPENEXR support
BuildRequires:  pkgconfig(OpenEXR)

# TIFF support
BuildRequires:  pkgconfig(libtiff-4)

# XSLT support
BuildRequires: pkgconfig(libxslt)

# PYTHON support
#  lib/kross/configure.in.in :
#   WARNING: Building Kross python plugin is now prohibited at all times,
#   because it is not compatible with Python >= 3.
%if %{with python}
%global python python3
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	pkgconfig(python)
%endif

# LCMS support
BuildRequires: lcms-devel

# BZIP2 support
BuildRequires:  pkgconfig(bzip2)

# PAPER support
BuildRequires:	libpaper-devel

# RUBY support
%if %{with ruby}
BuildRequires:	ruby ruby-devel >= 1.8.1
%endif

# FREETYPE support
BuildRequires:  pkgconfig(freetype2)

# LIBPNG support
BuildRequires:  pkgconfig(libpng)

# GRAPHICSMAGICK support
%{?with_graphicsmagick:BuildRequires:  pkgconfig(GraphicsMagick)}

# UTEMPTER support
BuildRequires:	%{_lib}utempter-devel

# POPPLER support
BuildRequires:  pkgconfig(poppler)

# POSTGRESQL support
#  Requires 'libpqxx', for kexi-driver-pgqsl
%if %{with postgresql}
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libpqxx)
Obsoletes:		trinity-libpqxx < %{?epoch:%{epoch}:}%{version}-%{release}
%endif

# WPD support
#  For chalk and filters
BuildRequires:  pkgconfig(libwpd-0.10)
Obsoletes:		trinity-libwpd < %{?epoch:%{epoch}:}%{version}-%{release}

# WV2 support

# no valid/updated/forked source code

# MESA support
BuildRequires:  pkgconfig(glu)

# LIBXI support
BuildRequires:  pkgconfig(xi)

# SQLITE support
BuildRequires:  pkgconfig(sqlite3)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xft)
BuildRequires:  %{_lib}ltdl-devel


%description
KOffice is an integrated office suite.

##########

%package suite
Summary:		An integrated office suite
Group:			Applications/Productivity
Obsoletes:      %{name} <= %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release} 
Requires:		%{name}-kword = %{?epoch:%{epoch}:}%{version}-%{release} 
Requires:		%{name}-kspread = %{?epoch:%{epoch}:}%{version}-%{release} 
Requires:		%{name}-kpresenter = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kivio = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-karbon = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kugar = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kexi = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kexi-driver-mysql = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_postgresql:Requires:       %{name}-kexi-driver-pgsql = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires:		%{name}-kchart = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kformula = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-filters = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-kplato = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-chalk = %{?epoch:%{epoch}:}%{version}-%{release}

%description suite
KOffice is an integrated office suite.

%files suite
#empty => virtual package

##########

%package core
Summary:		Core support files for %{name} 
Group:			Applications/Productivity
Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		perl

%description core
%{summary}.

%files core
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_prefix}/bin/koshell
%{tde_prefix}/bin/kthesaurus
%{tde_prefix}/bin/koconverter
%{tde_prefix}/%{_lib}/libtdeinit_koshell.so
%{tde_prefix}/%{_lib}/libtdeinit_kthesaurus.so
%{tde_prefix}/%{_lib}/trinity/tdefile_koffice.*
%{tde_prefix}/%{_lib}/trinity/tdefile_ooo.*
%{tde_prefix}/%{_lib}/trinity/tdefile_abiword.*
%{tde_prefix}/%{_lib}/trinity/tdefile_gnumeric.*
%{tde_prefix}/%{_lib}/trinity/kodocinfopropspage.*
%{tde_prefix}/%{_lib}/trinity/kofficescan.*
%{tde_prefix}/%{_lib}/trinity/kofficethumbnail.*
%{tde_prefix}/%{_lib}/trinity/koshell.*
%{tde_prefix}/%{_lib}/trinity/kthesaurus.*
%{tde_prefix}/%{_lib}/trinity/kwmailmerge_classic.*
%{tde_prefix}/%{_lib}/trinity/kwmailmerge_tdeabc.*
%{tde_prefix}/%{_lib}/trinity/kwmailmerge_qtsqldb_power.*
%{tde_prefix}/%{_lib}/trinity/kwmailmerge_qtsqldb.*
%{tde_prefix}/%{_lib}/trinity/libkounavailpart.*
%{tde_prefix}/%{_lib}/trinity/libkprkword.*
%{tde_prefix}/%{_lib}/trinity/libthesaurustool.*
%{tde_prefix}/%{_lib}/trinity/clipartthumbnail.*
%{tde_prefix}/share/apps/koffice/
%{tde_prefix}/share/apps/konqueror/servicemenus/*
%{tde_prefix}/share/apps/koshell/
%{tde_prefix}/share/apps/thesaurus/
%{tde_prefix}/share/config.kcfg/koshell.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/koffice/
%{tde_prefix}/share/doc/tde/HTML/en/koshell/
%{tde_prefix}/share/doc/tde/HTML/en/thesaurus/
%{tde_prefix}/share/icons/crystalsvg/*/*/*
%{tde_prefix}/share/icons/hicolor/*/*/*
%{tde_prefix}/share/icons/locolor/*/*/*
%{tde_prefix}/share/services/clipartthumbnail.desktop
%{tde_prefix}/share/services/tdefile_abiword.desktop
%{tde_prefix}/share/services/tdefile_gnumeric.desktop
%{tde_prefix}/share/services/tdefile_koffice.desktop
%{tde_prefix}/share/services/tdefile_ooo.desktop
%{tde_prefix}/share/services/kwmailmerge*.desktop
%{tde_prefix}/share/services/kodocinfopropspage.desktop
%{tde_prefix}/share/services/kofficethumbnail.desktop
%{tde_prefix}/share/services/kounavail.desktop
%{tde_prefix}/share/services/kprkword.desktop
%{tde_prefix}/share/services/thesaurustool.desktop
%{tde_prefix}/share/servicetypes/kochart.desktop
%{tde_prefix}/share/servicetypes/kofficepart.desktop
%{tde_prefix}/share/servicetypes/koplugin.desktop
%{tde_prefix}/share/servicetypes/kwmailmerge.desktop
%{tde_prefix}/share/servicetypes/widgetfactory.desktop
%{tde_prefix}/share/applications/tde/*koffice.desktop
%{tde_prefix}/share/applications/tde/KThesaurus.desktop
%{tde_prefix}/share/applications/tde/*koshell.desktop
%{tde_prefix}/share/apps/kofficewidgets/
%if %{with kross}
%if %{with python}
%{tde_prefix}/share/apps/kross/
%{tde_prefix}/%{_lib}/trinity/krosspython.*
%endif
%if %{with ruby}
%{tde_prefix}/%{_lib}/trinity/krossruby.*
%endif
%endif
%{tde_prefix}/share/man/man1/koconverter.1*
%{tde_prefix}/share/man/man1/koscript.1*
%{tde_prefix}/share/man/man1/koshell.1*
%{tde_prefix}/share/man/man1/kthesaurus.1*

##########

%package libs
Summary:		Runtime libraries for %{name} 
Group:			System Environment/Libraries
Conflicts:      %{name} <= %{version}-%{release}
Requires:		trinity-tdelibs
License:		LGPLv2+

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%doc COPYING.LIB
#_libdir/libk*common.so.*
%{tde_prefix}/%{_lib}/libkarboncommon.so.*
%{tde_prefix}/%{_lib}/libkspreadcommon.so.*
%{tde_prefix}/%{_lib}/libkdchart.so.*
%{tde_prefix}/%{_lib}/libkochart.so.*
%{tde_prefix}/%{_lib}/libkofficecore.so.*
%{tde_prefix}/%{_lib}/libkofficeui.so.*
%{tde_prefix}/%{_lib}/libkotext.so.*
%{tde_prefix}/%{_lib}/libkowmf.so.*
%{tde_prefix}/%{_lib}/libkopainter.so.*
%{tde_prefix}/%{_lib}/libkstore.so.*
%{tde_prefix}/%{_lib}/libkwmailmerge_interface.so.*
%{tde_prefix}/%{_lib}/libkwmf.so.*
%{tde_prefix}/%{_lib}/libkformulalib.so.*
%{tde_prefix}/%{_lib}/libkopalette.so.*
%{tde_prefix}/%{_lib}/libkoproperty.so.*
%if %{with kross}
%{tde_prefix}/%{_lib}/libkrossapi.so.*
%{tde_prefix}/%{_lib}/libkrossmain.so.*
%endif
%{tde_prefix}/share/man/man1/kspread.1*

##########

%package devel
Summary:		Development files for %{name} 
Group:			Development/Libraries
Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
License:		LGPLv2+

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/koffice-apidocs/
%{tde_prefix}/include/*
# FIXME: include only shlib symlinks we know/want to export
%{tde_prefix}/%{_lib}/lib*.so
%exclude %{tde_prefix}/%{_lib}/libtdeinit_*.so
%exclude %{tde_prefix}/%{_lib}/libkudesignercore.so

##########

%package kword
Summary:		A frame-based word processor capable of professional standard documents
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kword
%{summary}.

%files kword
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kword/
%{tde_prefix}/bin/kword
%{tde_prefix}/%{_lib}/libtdeinit_kword.so
%{tde_prefix}/%{_lib}/libkwordprivate.so.*
%{tde_prefix}/%{_lib}/trinity/libkwordpart.*
%{tde_prefix}/%{_lib}/trinity/kword.*
%{tde_prefix}/share/apps/kword/
%{tde_prefix}/share/services/kword*.desktop
%{tde_prefix}/share/services/kwserial*.desktop
%{tde_prefix}/share/templates/TextDocument.desktop
%{tde_prefix}/share/templates/.source/TextDocument.kwt
%{tde_prefix}/share/applications/tde/*kword.desktop
%{tde_prefix}/share/man/man1/kword.1*

##########

%package kspread
Summary:		A powerful spreadsheet application
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kspread
%{summary}.

%files kspread
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kspread/
%{tde_prefix}/bin/kspread
%{tde_prefix}/%{_lib}/libtdeinit_kspread.so
%{tde_prefix}/%{_lib}/trinity/kspread.*
%{tde_prefix}/%{_lib}/trinity/libkspreadpart.*
%{tde_prefix}/%{_lib}/trinity/kwmailmerge_kspread.*
%{tde_prefix}/%{_lib}/trinity/libcsvexport.*
%{tde_prefix}/%{_lib}/trinity/libcsvimport.*
%{tde_prefix}/%{_lib}/trinity/libgnumericexport.*
%{tde_prefix}/%{_lib}/trinity/libgnumericimport.*
%{tde_prefix}/%{_lib}/trinity/libkspreadhtmlexport.*
%{tde_prefix}/%{_lib}/trinity/libkspreadinsertcalendar.*
%{tde_prefix}/%{_lib}/trinity/libopencalcexport.*
%{tde_prefix}/%{_lib}/trinity/libopencalcimport.*
%{tde_prefix}/%{_lib}/trinity/libqproimport.*
%{tde_prefix}/share/apps/kspread/
%{tde_prefix}/share/services/kspread*.desktop
%{tde_prefix}/share/templates/SpreadSheet.desktop
%{tde_prefix}/share/templates/.source/SpreadSheet.kst
%{tde_prefix}/share/applications/tde/*kspread.desktop
%if %{with kross}
%{tde_prefix}/%{_lib}/trinity/kspreadscripting.*
%{tde_prefix}/%{_lib}/trinity/krosskspreadcore.*
%endif

##########

%package kpresenter
Summary:		A full-featured presentation program
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kpresenter
%{summary}.

%files kpresenter
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kpresenter/
%{tde_prefix}/bin/kpresenter
%{tde_prefix}/bin/kprconverter.pl
%{tde_prefix}/%{_lib}/libtdeinit_kpresenter.so
%{tde_prefix}/%{_lib}/libkpresenterimageexport.so.*
%{tde_prefix}/%{_lib}/libkpresenterprivate.so.*
%{tde_prefix}/%{_lib}/trinity/*kpresenter*.*
%{tde_prefix}/share/apps/kpresenter/
%{tde_prefix}/share/services/kpresenter*.desktop
%{tde_prefix}/share/templates/Presentation.desktop
%{tde_prefix}/share/templates/.source/Presentation.kpt
%{tde_prefix}/share/applications/tde/*kpresenter.desktop
%{tde_prefix}/share/man/man1/kprconverter.pl.1*
%{tde_prefix}/share/man/man1/kpresenter.1*

##########

%package kivio
Summary:		A flowcharting application
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      kivio < %{?epoch:%{epoch}:}%{version}-%{release}

%description kivio
%{summary}.

%files kivio
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kivio/
%{tde_prefix}/bin/kivio
%{tde_prefix}/%{_lib}/libtdeinit_kivio.so
%{tde_prefix}/%{_lib}/libkiviocommon.so.*
%{tde_prefix}/%{_lib}/trinity/*kivio*.*
%{tde_prefix}/%{_lib}/trinity/straight_connector.*
%{tde_prefix}/share/apps/kivio/
%{tde_prefix}/share/config.kcfg/kivio.kcfg
%{tde_prefix}/share/services/kivio*.desktop
%{tde_prefix}/share/applications/tde/*kivio.desktop
%{tde_prefix}/share/man/man1/kivio.1*

##########

%package karbon
Summary:		A vector drawing application
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description karbon
%{summary}.

%files karbon
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/karbon/
%{tde_prefix}/bin/karbon
%{tde_prefix}/%{_lib}/libtdeinit_karbon.so
%exclude %{tde_prefix}/%{_lib}/trinity/libkarbonepsimport.*
%{tde_prefix}/%{_lib}/trinity/*karbon*.*
%{tde_prefix}/%{_lib}/trinity/libwmfexport.*
%{tde_prefix}/%{_lib}/trinity/libwmfimport.*
%{tde_prefix}/share/apps/karbon/
%{tde_prefix}/share/services/karbon*
%{tde_prefix}/share/servicetypes/karbon_module.desktop
%{tde_prefix}/share/templates/Illustration.desktop
%{tde_prefix}/share/templates/.source/Illustration.karbon
%{tde_prefix}/share/applications/tde/*karbon.desktop
%{tde_prefix}/share/man/man1/karbon.1*

##########

%package kugar
Summary:		A tool for generating business quality reports
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kugar
%{summary}.

%files kugar
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kugar/
%{tde_prefix}/bin/kugar
%{tde_prefix}/bin/kudesigner
%{tde_prefix}/%{_lib}/libtdeinit_kugar.so
%{tde_prefix}/%{_lib}/libtdeinit_kudesigner.so
%{tde_prefix}/%{_lib}/libkugarlib.so.*
%{tde_prefix}/%{_lib}/libkudesignercore.so
%{tde_prefix}/%{_lib}/trinity/kudesigner.*
%{tde_prefix}/%{_lib}/trinity/kugar.*
%{tde_prefix}/%{_lib}/trinity/libkudesignerpart.*
%{tde_prefix}/%{_lib}/trinity/libkugarpart.*
%{tde_prefix}/share/apps/kudesigner/
%{tde_prefix}/share/apps/kugar/
%{tde_prefix}/share/services/kugar*.desktop
%{tde_prefix}/share/applications/tde/*kugar.desktop
%{tde_prefix}/share/applications/tde/*kudesigner.desktop
%{tde_prefix}/share/man/man1/kudesigner.1*
%{tde_prefix}/share/man/man1/kugar.1*

##########

%package kexi
Summary:		An integrated environment for managing data
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%if %{without postgresql}
Obsoletes:		%{name}-kexi-driver-pgsql < %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description kexi
%{summary}.
For additional database drivers take a look at %{name}-kexi-driver-*

%files kexi
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kexi/
%{tde_prefix}/bin/kexi*
%{tde_prefix}/bin/ksqlite*
%{tde_prefix}/%{_lib}/libtdeinit_kexi.so
%{tde_prefix}/%{_lib}/libkexi*.so.*
%{tde_prefix}/%{_lib}/libkformdesigner.so.*
%{tde_prefix}/%{_lib}/trinity/kformdesigner_*.*
%{tde_prefix}/%{_lib}/trinity/kexidb_sqlite2driver.*
%{tde_prefix}/%{_lib}/trinity/kexidb_sqlite3driver.*
%{tde_prefix}/%{_lib}/trinity/kexihandler_*.*
%{tde_prefix}/%{_lib}/trinity/kexi.*
# moved here to workaround bug #394101, alternative is to move libkexi(db|dbparser|utils) to -libs)
%{tde_prefix}/%{_lib}/trinity/libkspreadkexiimport.*
%config(noreplace) %{_sysconfdir}/trinity/kexirc
%config(noreplace) %{_sysconfdir}/trinity/magic/kexi.magic
%{tde_prefix}/share/mimelnk/application/*
%{tde_prefix}/share/servicetypes/kexi*.desktop
%{tde_prefix}/share/services/kexi/
%{tde_prefix}/share/apps/kexi/
%{tde_prefix}/share/services/kformdesigner/
%{tde_prefix}/share/applications/tde/*kexi.desktop
%{tde_prefix}/share/services/kexidb_sqlite*driver.desktop
%if %{with kross}
%{tde_prefix}/bin/krossrunner
%{tde_prefix}/%{_lib}/trinity/krosskexiapp.*
%{tde_prefix}/%{_lib}/trinity/krosskexidb.*
%endif
%config(noreplace) %{_sysconfdir}/trinity/magic/kexi.magic.mgc

##########

%package kexi-driver-mysql
Summary:		Mysql-driver for kexi
Group:			Applications/Productivity
Requires:		%{name}-kexi = %{?epoch:%{epoch}:}%{version}-%{release}

%description kexi-driver-mysql
%{summary}.

%files kexi-driver-mysql
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kexidb_mysqldriver.*
%{tde_prefix}/%{_lib}/trinity/keximigrate_mysql.*
%{tde_prefix}/share/services/keximigrate_mysql.desktop
%{tde_prefix}/share/services/kexidb_mysqldriver.desktop

##########

%if %{with postgresql}

%package kexi-driver-pgsql
Summary:		Postgresql driver for kexi
Group:			Applications/Productivity
Requires:		%{name}-kexi = %{?epoch:%{epoch}:}%{version}-%{release}

%description kexi-driver-pgsql
%{summary}.

%files kexi-driver-pgsql
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kexidb_pqxxsqldriver.*
%{tde_prefix}/%{_lib}/trinity/keximigrate_pqxx.*
%{tde_prefix}/share/services/kexidb_pqxxsqldriver.desktop
%{tde_prefix}/share/services/keximigrate_pqxx.desktop

%endif

##########

%package kchart
Summary:		An integrated graph and chart drawing tool
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kchart
%{summary}.

%files kchart
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kchart/
%{tde_prefix}/bin/kchart
%{tde_prefix}/%{_lib}/libkchart*.so.*
%{tde_prefix}/%{_lib}/libtdeinit_kchart.so
%{tde_prefix}/%{_lib}/trinity/*kchart*.*
%{tde_prefix}/share/apps/kchart/
%{tde_prefix}/share/services/kchart*.desktop
%{tde_prefix}/share/applications/tde/*kchart.desktop
%{tde_prefix}/share/man/man1/kchart.1*

##########

%package kformula
Summary:		A powerful formula editor
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:		fonts-ttf-dejavu

%description kformula
%{summary}.

%files kformula
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kformula/
%{tde_prefix}/bin/kformula
%{tde_prefix}/%{_lib}/libtdeinit_kformula.so
%{tde_prefix}/%{_lib}/trinity/*kformula*.*
%{tde_prefix}/share/apps/kformula/
%{tde_prefix}/share/services/kformula*.desktop
%{tde_prefix}/share/applications/tde/*kformula.desktop
%{tde_prefix}/share/man/man1/kformula.1*

##########

%package filters
Summary:		Import and Export Filters for KOffice
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description filters
%{summary}.

%files filters
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkwordexportfilters.so.*
%{tde_prefix}/%{_lib}/trinity/libabiwordexport.*
%{tde_prefix}/%{_lib}/trinity/libabiwordimport.*
%{tde_prefix}/%{_lib}/trinity/libamiproexport.*
%{tde_prefix}/%{_lib}/trinity/libamiproimport.*
%{tde_prefix}/%{_lib}/trinity/libapplixspreadimport.*
%{tde_prefix}/%{_lib}/trinity/libapplixwordimport.*
%{tde_prefix}/%{_lib}/trinity/libasciiexport.*
%{tde_prefix}/%{_lib}/trinity/libasciiimport.*
%{tde_prefix}/%{_lib}/trinity/libdbaseimport.*
%{tde_prefix}/%{_lib}/trinity/libdocbookexport.*
%{tde_prefix}/%{_lib}/trinity/libexcelimport.*
%{tde_prefix}/%{_lib}/trinity/libgenerickofilter.*
%{tde_prefix}/%{_lib}/trinity/libhtmlexport.*
%{tde_prefix}/%{_lib}/trinity/libhtmlimport.*
%{tde_prefix}/%{_lib}/trinity/libkarbonepsimport.*
%{tde_prefix}/%{_lib}/trinity/libkfolatexexport.*
%{tde_prefix}/%{_lib}/trinity/libkfomathmlexport.*
%{tde_prefix}/%{_lib}/trinity/libkfomathmlimport.*
%{tde_prefix}/%{_lib}/trinity/libkfopngexport.*
%{tde_prefix}/%{_lib}/trinity/libkspreadlatexexport.*
%{tde_prefix}/%{_lib}/trinity/libkugarnopimport.*
%{tde_prefix}/%{_lib}/trinity/libkwordkword1dot3import.*
%{tde_prefix}/%{_lib}/trinity/libkwordlatexexport.*
%{tde_prefix}/%{_lib}/trinity/libmswriteexport.*
%{tde_prefix}/%{_lib}/trinity/libmswriteimport.*
%{tde_prefix}/%{_lib}/trinity/libooimpressexport.*
%{tde_prefix}/%{_lib}/trinity/libooimpressimport.*
%{tde_prefix}/%{_lib}/trinity/liboowriterexport.*
%{tde_prefix}/%{_lib}/trinity/liboowriterimport.*
%{tde_prefix}/%{_lib}/trinity/libpalmdocexport.*
%{tde_prefix}/%{_lib}/trinity/libpalmdocimport.*
%{tde_prefix}/%{_lib}/trinity/libpdfimport.*
%{tde_prefix}/%{_lib}/trinity/librtfexport.*
%{tde_prefix}/%{_lib}/trinity/librtfimport.*
%{tde_prefix}/%{_lib}/trinity/libwmlexport.*
%{tde_prefix}/%{_lib}/trinity/libwmlimport.*
%{tde_prefix}/%{_lib}/trinity/libwpexport.*
%{tde_prefix}/%{_lib}/trinity/libwpimport.*
%if %{with wv2}
%{tde_prefix}/%{_lib}/trinity/libmswordimport.*
%endif
%{tde_prefix}/%{_lib}/trinity/libxsltimport.*
%{tde_prefix}/%{_lib}/trinity/libxsltexport.*
%{tde_prefix}/%{_lib}/trinity/libhancomwordimport.*
%{tde_prefix}/%{_lib}/trinity/libkfosvgexport.*
%{tde_prefix}/%{_lib}/trinity/liboodrawimport.*
%{tde_prefix}/%{_lib}/trinity/libolefilter.*
%{tde_prefix}/share/apps/xsltfilter/
%{tde_prefix}/share/services/generic_filter.desktop
%{tde_prefix}/share/services/ole_powerpoint97_import.desktop
%{tde_prefix}/share/services/xslt*.desktop
%{tde_prefix}/share/servicetypes/kofilter*.desktop

##########

%package kplato
Summary:		An integrated project management and planning tool
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}

%description kplato
%{summary}.

%files kplato
%defattr(-,root,root,-)
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kplato/
%{tde_prefix}/bin/kplato
%{tde_prefix}/%{_lib}/libtdeinit_kplato.so
%{tde_prefix}/%{_lib}/trinity/kplato.*
%{tde_prefix}/%{_lib}/trinity/libkplatopart.*
%{tde_prefix}/share/apps/kplato/
%{tde_prefix}/share/services/kplatopart.desktop
%{tde_prefix}/share/applications/tde/*kplato.desktop

##########

%package chalk
Summary:		pixel-based image manipulation program for the TDE Office Suite [Trinity]
Group:			Applications/Productivity
Requires:		%{name}-core = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-chalk-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-filters = %{?epoch:%{epoch}:}%{version}-%{release}

%description chalk
Chalk is a painting and image editing application for KOffice. Chalk contains
both ease-of-use and fun features like guided painting.

This package is part of the TDE Office Suite.

%files chalk
%defattr(-,root,root,-)
%{tde_prefix}/bin/chalk
%{tde_prefix}/%{_lib}/trinity/chalkblurfilter.la
%{tde_prefix}/%{_lib}/trinity/chalkblurfilter.so
%{tde_prefix}/%{_lib}/trinity/chalkbumpmap.la
%{tde_prefix}/%{_lib}/trinity/chalkbumpmap.so
%{tde_prefix}/%{_lib}/trinity/chalkcimg.la
%{tde_prefix}/%{_lib}/trinity/chalkcimg.so
%{tde_prefix}/%{_lib}/trinity/chalk_cmyk_*
%{tde_prefix}/%{_lib}/trinity/chalkcmykplugin.la
%{tde_prefix}/%{_lib}/trinity/chalkcmykplugin.so
%{tde_prefix}/%{_lib}/trinity/chalkcolorify.la
%{tde_prefix}/%{_lib}/trinity/chalkcolorify.so
%{tde_prefix}/%{_lib}/trinity/chalkcolorrange.la
%{tde_prefix}/%{_lib}/trinity/chalkcolorrange.so
%{tde_prefix}/%{_lib}/trinity/chalkcolorsfilters.la
%{tde_prefix}/%{_lib}/trinity/chalkcolorsfilters.so
%{tde_prefix}/%{_lib}/trinity/chalkcolorspaceconversion.la
%{tde_prefix}/%{_lib}/trinity/chalkcolorspaceconversion.so
%{tde_prefix}/%{_lib}/trinity/chalkconvolutionfilters.la
%{tde_prefix}/%{_lib}/trinity/chalkconvolutionfilters.so
%{tde_prefix}/%{_lib}/trinity/chalkdefaultpaintops.la
%{tde_prefix}/%{_lib}/trinity/chalkdefaultpaintops.so
%{tde_prefix}/%{_lib}/trinity/chalkdefaulttools.la
%{tde_prefix}/%{_lib}/trinity/chalkdefaulttools.so
%{tde_prefix}/%{_lib}/trinity/chalkdropshadow.la
%{tde_prefix}/%{_lib}/trinity/chalkdropshadow.so
%{tde_prefix}/%{_lib}/trinity/chalkembossfilter.la
%{tde_prefix}/%{_lib}/trinity/chalkembossfilter.so
%{tde_prefix}/%{_lib}/trinity/chalkexample.la
%{tde_prefix}/%{_lib}/trinity/chalkexample.so
%{tde_prefix}/%{_lib}/trinity/chalkextensioncolorsfilters.la
%{tde_prefix}/%{_lib}/trinity/chalkextensioncolorsfilters.so
%{tde_prefix}/%{_lib}/trinity/chalkfastcolortransfer.la
%{tde_prefix}/%{_lib}/trinity/chalkfastcolortransfer.so
%{tde_prefix}/%{_lib}/trinity/chalkfiltersgallery.la
%{tde_prefix}/%{_lib}/trinity/chalkfiltersgallery.so
%{tde_prefix}/%{_lib}/trinity/chalk_gray_*
%{tde_prefix}/%{_lib}/trinity/chalkgrayplugin.la
%{tde_prefix}/%{_lib}/trinity/chalkgrayplugin.so
%{tde_prefix}/%{_lib}/trinity/chalkhistogramdocker.la
%{tde_prefix}/%{_lib}/trinity/chalkhistogramdocker.so
%{tde_prefix}/%{_lib}/trinity/chalkhistogram.la
%{tde_prefix}/%{_lib}/trinity/chalkhistogram.so
%{tde_prefix}/%{_lib}/trinity/chalkimageenhancement.la
%{tde_prefix}/%{_lib}/trinity/chalkimageenhancement.so
%{tde_prefix}/%{_lib}/trinity/chalkimagesize.la
%{tde_prefix}/%{_lib}/trinity/chalkimagesize.so
%{tde_prefix}/%{_lib}/trinity/chalk.la
%{tde_prefix}/%{_lib}/trinity/chalklenscorrectionfilter.la
%{tde_prefix}/%{_lib}/trinity/chalklenscorrectionfilter.so
%{tde_prefix}/%{_lib}/trinity/chalklevelfilter.la
%{tde_prefix}/%{_lib}/trinity/chalklevelfilter.so
%{tde_prefix}/%{_lib}/trinity/chalk_lms_*
%{tde_prefix}/%{_lib}/trinity/chalkmodifyselection.la
%{tde_prefix}/%{_lib}/trinity/chalkmodifyselection.so
%{tde_prefix}/%{_lib}/trinity/chalknoisefilter.la
%{tde_prefix}/%{_lib}/trinity/chalknoisefilter.so
%{tde_prefix}/%{_lib}/trinity/chalkoilpaintfilter.la
%{tde_prefix}/%{_lib}/trinity/chalkoilpaintfilter.so
%{tde_prefix}/%{_lib}/trinity/chalkpixelizefilter.la
%{tde_prefix}/%{_lib}/trinity/chalkpixelizefilter.so
%{tde_prefix}/%{_lib}/trinity/chalkraindropsfilter.la
%{tde_prefix}/%{_lib}/trinity/chalkraindropsfilter.so
%{tde_prefix}/%{_lib}/trinity/chalkrandompickfilter.la
%{tde_prefix}/%{_lib}/trinity/chalkrandompickfilter.so
%{tde_prefix}/%{_lib}/trinity/chalk_rgb_*
%{tde_prefix}/%{_lib}/trinity/chalkrgbplugin.la
%{tde_prefix}/%{_lib}/trinity/chalkrgbplugin.so
%{tde_prefix}/%{_lib}/trinity/chalkrotateimage.la
%{tde_prefix}/%{_lib}/trinity/chalkrotateimage.so
%{tde_prefix}/%{_lib}/trinity/chalkroundcornersfilter.la
%{tde_prefix}/%{_lib}/trinity/chalkroundcornersfilter.so
%{tde_prefix}/%{_lib}/trinity/chalkselectiontools.la
%{tde_prefix}/%{_lib}/trinity/chalkselectiontools.so
%{tde_prefix}/%{_lib}/trinity/chalkselectopaque.la
%{tde_prefix}/%{_lib}/trinity/chalkselectopaque.so
%{tde_prefix}/%{_lib}/trinity/chalkseparatechannels.la
%{tde_prefix}/%{_lib}/trinity/chalkseparatechannels.so
%{tde_prefix}/%{_lib}/trinity/chalkshearimage.la
%{tde_prefix}/%{_lib}/trinity/chalkshearimage.so
%{tde_prefix}/%{_lib}/trinity/chalksmalltilesfilter.la
%{tde_prefix}/%{_lib}/trinity/chalksmalltilesfilter.so
%{tde_prefix}/%{_lib}/trinity/chalk.so
%{tde_prefix}/%{_lib}/trinity/chalkscreenshot.la
%{tde_prefix}/%{_lib}/trinity/chalkscreenshot.so
%{tde_prefix}/%{_lib}/trinity/chalksobelfilter.la
%{tde_prefix}/%{_lib}/trinity/chalksobelfilter.so
%{tde_prefix}/%{_lib}/trinity/chalksubstrate.la
%{tde_prefix}/%{_lib}/trinity/chalksubstrate.so
%{tde_prefix}/%{_lib}/trinity/chalktoolcrop.la
%{tde_prefix}/%{_lib}/trinity/chalktoolcrop.so
%{tde_prefix}/%{_lib}/trinity/chalktoolcurves.la
%{tde_prefix}/%{_lib}/trinity/chalktoolcurves.so
%{tde_prefix}/%{_lib}/trinity/chalktoolfilter.la
%{tde_prefix}/%{_lib}/trinity/chalktoolfilter.so
%{tde_prefix}/%{_lib}/trinity/chalktoolperspectivegrid.la
%{tde_prefix}/%{_lib}/trinity/chalktoolperspectivegrid.so
%{tde_prefix}/%{_lib}/trinity/chalktoolperspectivetransform.la
%{tde_prefix}/%{_lib}/trinity/chalktoolperspectivetransform.so
%{tde_prefix}/%{_lib}/trinity/chalktoolpolygon.la
%{tde_prefix}/%{_lib}/trinity/chalktoolpolygon.so
%{tde_prefix}/%{_lib}/trinity/chalktoolpolyline.la
%{tde_prefix}/%{_lib}/trinity/chalktoolpolyline.so
%{tde_prefix}/%{_lib}/trinity/chalktoolselectsimilar.la
%{tde_prefix}/%{_lib}/trinity/chalktoolselectsimilar.so
%{tde_prefix}/%{_lib}/trinity/chalktoolstar.la
%{tde_prefix}/%{_lib}/trinity/chalktoolstar.so
%{tde_prefix}/%{_lib}/trinity/chalktooltransform.la
%{tde_prefix}/%{_lib}/trinity/chalktooltransform.so
%{tde_prefix}/%{_lib}/trinity/chalkunsharpfilter.la
%{tde_prefix}/%{_lib}/trinity/chalkunsharpfilter.so
%{tde_prefix}/%{_lib}/trinity/chalkwavefilter.la
%{tde_prefix}/%{_lib}/trinity/chalkwavefilter.so
%{tde_prefix}/%{_lib}/trinity/chalkwetplugin.la
%{tde_prefix}/%{_lib}/trinity/chalkwetplugin.so
%{tde_prefix}/%{_lib}/trinity/chalk_ycbcr_*
%if %{with graphicsmagick}
%{tde_prefix}/%{_lib}/trinity/libchalkgmagickexport.la
%{tde_prefix}/%{_lib}/trinity/libchalkgmagickexport.so
%{tde_prefix}/%{_lib}/trinity/libchalkgmagickimport.la
%{tde_prefix}/%{_lib}/trinity/libchalkgmagickimport.so
%{tde_prefix}/%{_lib}/trinity/libchalkjpegexport.la
%{tde_prefix}/%{_lib}/trinity/libchalkjpegexport.so
%{tde_prefix}/%{_lib}/trinity/libchalkjpegimport.la
%{tde_prefix}/%{_lib}/trinity/libchalkjpegimport.so
%endif
%{tde_prefix}/%{_lib}/trinity/libchalk_openexr_export.la
%{tde_prefix}/%{_lib}/trinity/libchalk_openexr_export.so
%{tde_prefix}/%{_lib}/trinity/libchalk_openexr_import.la
%{tde_prefix}/%{_lib}/trinity/libchalk_openexr_import.so
%{tde_prefix}/%{_lib}/trinity/libchalkpart.la
%{tde_prefix}/%{_lib}/trinity/libchalkpart.so
%{tde_prefix}/%{_lib}/trinity/libchalkpdfimport.la
%{tde_prefix}/%{_lib}/trinity/libchalkpdfimport.so
%{tde_prefix}/%{_lib}/trinity/libchalkpngexport.la
%{tde_prefix}/%{_lib}/trinity/libchalkpngexport.so
%{tde_prefix}/%{_lib}/trinity/libchalkpngimport.la
%{tde_prefix}/%{_lib}/trinity/libchalkpngimport.so
%{tde_prefix}/%{_lib}/trinity/libchalk_raw_import.la
%{tde_prefix}/%{_lib}/trinity/libchalk_raw_import.so
%if %{with graphicsmagick}
%{tde_prefix}/%{_lib}/trinity/libchalktiffexport.la
%{tde_prefix}/%{_lib}/trinity/libchalktiffexport.so
%{tde_prefix}/%{_lib}/trinity/libchalktiffimport.la
%{tde_prefix}/%{_lib}/trinity/libchalktiffimport.so
%endif
%{tde_prefix}/%{_lib}/libtdeinit_chalk.so
%{tde_prefix}/%{_lib}/libchalk_cmyk_*.so.*
%{tde_prefix}/%{_lib}/libchalkcolor.so.*
%{tde_prefix}/%{_lib}/libchalkcommon.so.*
%{tde_prefix}/%{_lib}/libchalkgrayscale.so.*
%{tde_prefix}/%{_lib}/libchalk_gray_*.so.*
%{tde_prefix}/%{_lib}/libchalkimage.so.*
%{tde_prefix}/%{_lib}/libchalk_lms_*.so.*
%{tde_prefix}/%{_lib}/libchalk_rgb_*.so.*
%{tde_prefix}/%{_lib}/libchalkrgb.so.*
%{tde_prefix}/%{_lib}/libchalkui.so.*
%{tde_prefix}/%{_lib}/libchalk_ycbcr_*.so.*
%if %{with kross}
%{tde_prefix}/%{_lib}/trinity/krosschalkcore.la
%{tde_prefix}/%{_lib}/trinity/krosschalkcore.so
%{tde_prefix}/%{_lib}/trinity/chalkscripting.la
%{tde_prefix}/%{_lib}/trinity/chalkscripting.so
%{tde_prefix}/%{_lib}/libchalkscripting.so.*
%endif

##########

%package chalk-data
Summary:		data files for Chalk painting program [Trinity]
Group:			Applications/Productivity

%description chalk-data
This package contains architecture-independent data files for Chalk,
the painting program shipped with the TDE Office Suite.

See the chalk package for further information.

This package is part of the TDE Office Suite.

%files chalk-data
%defattr(-,root,root,-)
%{tde_prefix}/share/applications/tde/chalk.desktop
%{tde_prefix}/share/applnk/.hidden/chalk_*.desktop
%{tde_prefix}/share/apps/chalk/
%{tde_prefix}/share/apps/chalkplugins/
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/chalk/
%{tde_prefix}/share/services/chalk*.desktop
%{tde_prefix}/share/servicetypes/chalk*.desktop


%prep
%autosetup -p1 -n %{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}

touch config.h.in

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/"*"/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"
export kde_confdir="%{_sysconfdir}/trinity"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_prefix}/bin \
  --datadir=%{tde_prefix}/share \
  --libdir=%{tde_prefix}/%{_lib} \
  --mandir=%{tde_prefix}/share/man \
  --includedir=%{tde_prefix}/include/tde \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  %{?with_clang:--disable-gcc-hidden-visibility} \
  %{!?with_clang:--enable-gcc-hidden-visibility} \
  \
  --with-extra-libs=%{tde_prefix}/%{_lib} \
  --with-extra-includes=%{tde_prefix}/include/arts \
  \
  --disable-kexi-macros \
  %{?with_kross:--enable-scripting} %{!?with_kross:--disable-scripting} \
  %{?with_postgresql:--enable-pgsql} %{!?with_postgresql:--disable-pgsql} \

# Ensure PQXX was detected (required by kexidb/pgsql)
%if %{with postgresql}
if grep 'S\["compile_pgsql_plugin_TRUE"\]="#"' config.status; then
  exit 1
fi
%endif

# Ensure WV2 was detected
%if %{with wv2}
if grep 'S\["include_wv2_msword_filter_TRUE"\]="#"' config.status; then
  exit 2
fi
%endif

%__make %{?_smp_mflags} || %__make


%install
%__make install DESTDIR=%{buildroot}

# Fix desktop icon location
%__mv -f "%{?buildroot}%{tde_prefix}/share/applnk/"*"/KThesaurus.desktop" "%{?buildroot}%{tde_prefix}/share/applications/tde"

# Apps that should stay in TDE
for i in kivio kplato; do
  echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/${i}.desktop"
done

# Links duplicate files
%fdupes %{buildroot}

## unpackaged files
# fonts
rm -rfv %{buildroot}%{tde_prefix}/share/apps/kformula/fonts/
# libtool archives
rm -f %{buildroot}%{tde_prefix}/%{_lib}/lib*.la
# shouldn't these be in koffice-l10n? 
rm -f %{buildroot}%{tde_prefix}/share/locale/pl/LC_MESSAGES/kexi_{add,delete}_column_gui_transl_pl.sh

