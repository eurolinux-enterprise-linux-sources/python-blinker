%global mod_name blinker
%global with_python3 0

Name:           python-blinker
Version:        1.3
Release:        2%{?dist}
Summary:        Fast, simple object-to-object and broadcast signaling

Group:          Development/Libraries
License:        MIT
URL:            http://discorporate.us/projects/Blinker/
Source0:        http://pypi.python.org/packages/source/b/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

%description
Blinker provides a fast dispatching system that allows any number 
of interested parties to subscribe to events, or "signals".

%if 0%{?with_python3}
%package -n python3-blinker
Summary:        Fast, simple object-to-object and broadcast signaling

%description -n python3-blinker
Blinker provides a fast dispatching system that allows any number 
of interested parties to subscribe to events, or "signals".
%endif

%prep
%setup -q -n %{mod_name}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif

%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc docs/ CHANGES LICENSE README PKG-INFO
%{python_sitelib}/*.egg-info
%{python_sitelib}/%{mod_name}

%if 0%{?with_python3}
%files -n python3-blinker
%doc docs/ CHANGES LICENSE README PKG-INFO
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{mod_name}
%endif


%changelog
* Fri Apr 18 2014 Lokesh Mandvekar <lsm5@redhat.com> - 1.3-2
- Rebuilt for RHEL-7

* Tue Sep 24 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 1.3-1
- Updated source and added python3 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 1.1-1
- Initial RPM
