Summary:	EPYC System Management Interface (E-SMI) In-band library
Summary(pl.UTF-8):	Biblioteka komunikacji in-band z EPYC SMI (E-SMI)
Name:		esmi_ib_library
Version:	5.2.1
Release:	1
License:	NCSA
Group:		Libraries
#Source0Download: https://github.com/amd/esmi_ib_library/tags
Source0:	https://github.com/amd/esmi_ib_library/archive/esmi_pkg_ver-%{version}/%{name}-esmi_pkg_ver-%{version}.tar.gz
# Source0-md5:	e5958140596a4cd6a97c254fcfdccfc7
URL:		https://github.com/amd/esmi_ib_library
BuildRequires:	cmake >= 3.5.0
# <asm/amd_hsmp.h>
BuildRequires:	linux-libc-headers >= 7:5.18
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	rpm-build >= 4.6
# generally for some models of AMD x86_64 CPUs, but available for all ABIs
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The EPYC System Management Interface In-band Library, or E-SMI
library, is part of the EPYC System Management Inband software stack.
It is a C library for Linux that provides a user space interface to
monitor and control the AMD CPU's power, energy, performance and other
system management features.

%description -l pl.UTF-8
EPYC System Management Interface In-band Library, w skrócie biblioteka
E-SMI, to część stosu oprogramowania EPYC System Management Inband.
Jest to biblioteka C dla Linuksa, zapewniająca interfejs przestrzeni
użytkownika do monitorowania i sterowania zasilaniem, poborem energii,
wydajnością i innymi funkcjami zarządzania systemu procesorów AMD.

%package devel
Summary:	Header files for E-SMI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki E-SMI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# <asm/amd_hsmp.h>
Requires:	linux-libc-headers >= 7:5.18

%description devel
Header files for E-SMI library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki E-SMI.

%package static
Summary:	Static E-SMI library
Summary(pl.UTF-8):	Statyczna biblioteka E-SMI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static E-SMI library.

%description static -l pl.UTF-8
Statyczna biblioteka E-SMI.

%package apidocs
Summary:	API documentation for E-SMI library
Summary(pl.UTF-8):	Dokumentacja API biblioteki E-SMI
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for E-SMI library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki E-SMI.

%prep
%setup -q -n %{name}-esmi_pkg_ver-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/e_smi

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING docs/{README.md,RELEASENOTES.md}
%attr(755,root,root) %{_bindir}/e_smi_tool
%{_libdir}/libe_smi64.so.*.*.*
%ghost %{_libdir}/libe_smi64.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libe_smi64.so
%{_includedir}/e_smi

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc ESMI_Manual.pdf
%endif
