Summary:	LDAP browser, utility and more
Summary(pl.UTF-8):   Przeglądarka, narzędzie i jeszcze więcej do LDAP
Name:		luma
Version:	2.3
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/luma/%{name}-%{version}.tar.bz2
# Source0-md5:	c1f3a8033a047a7046848833445ed496
Source1:	%{name}.desktop
Patch0:		%{name}-dont_check_req_while_build.patch
Patch1:		%{name}-python.patch
URL:		http://luma.sourceforge.net/
BuildRequires:	python >= 2.3
BuildRequires:	rpmbuild(macros) >= 1.231
Requires:	python-ldap >= 2.0.1
Requires:	python-PyQt >= 3.10
Requires:	py-smbpasswd
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDAP browser, utility and more.

%description -l pl.UTF-8
Przeglądarka, narzędzie i jeszcze więcej do LDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_prefix},%{_desktopdir},%{_pixmapsdir}}

./install.py \
	--prefix=$RPM_BUILD_ROOT%{_prefix}

rm -f $RPM_BUILD_ROOT%{_bindir}/luma
echo '#!%{__python} %{_prefix}/lib/%{name}/luma.py' > $RPM_BUILD_ROOT%{_bindir}/luma
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/luma-48.png $RPM_BUILD_ROOT%{_pixmapsdir}/luma.png

%py_ocomp $RPM_BUILD_ROOT%{_prefix}/lib/%{name}
find $RPM_BUILD_ROOT -name "*.py" -not -name luma.py -exec rm -f '{}' ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
