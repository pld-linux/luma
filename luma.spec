Summary:	LDAP browser, utility and more
Name:		luma
Version:	2.2
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/sourceforge/luma/%{name}-%{version}.tar.bz2
# Source0-md5:	2dce8ec50eddaff4b8d8a487e514cc4f
Source1:	%{name}.desktop
Patch0:		%{name}-dont_check_req_while_build.patch
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

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_prefix},%{_desktopdir},%{_pixmapsdir}}

./install.py \
	--prefix=$RPM_BUILD_ROOT%{_prefix}

rm -f $RPM_BUILD_ROOT%{_bindir}/luma
echo "%{__python} %{_libdir}/%{name}/luma.pyc" > $RPM_BUILD_ROOT%{_bindir}/luma
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/luma-48.png $RPM_BUILD_ROOT%{_pixmapsdir}/luma.png

%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{name}
find $RPM_BUILD_ROOT%{_libdir}/%{name} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/*
%{_pixmapsdir}/*
