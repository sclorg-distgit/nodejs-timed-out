%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name timed-out

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        2.0.0
Release:        6%{?dist}
Summary:        Timeout HTTP/HTTPS requests

License:        MIT
URL:            https://github.com/floatdrop/timed-out
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
Source1:        https://raw.githubusercontent.com/floatdrop/timed-out/master/license
Source2:        https://raw.githubusercontent.com/floatdrop/timed-out/master/test.js
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
Timeout HTTP/HTTPS requests. Emit Error object with code property
equal ETIMEDOUT or ESOCKETTIMEDOUT when ClientRequest is hanged.

%prep
%setup -q -n package
rm -rf node_modules

cp -p %{SOURCE1} %{SOURCE2} .

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md license
%{nodejs_sitelib}/%{module_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-6
- rebuilt

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-5
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-4
- Enable scl macros, fix license macro for el6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-2
- Add test.js from upstream and enable tests

* Thu Dec 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-1
- Initial packaging