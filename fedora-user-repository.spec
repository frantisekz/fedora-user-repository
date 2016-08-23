%define debug_package %{nil}

Name:    fedora-user-repository
Version: 0.6.0
Release: 1
Summary: Fedora User Repository
BuildArchitectures: noarch
License: GPLv2+
URL:     https://experimental-fur.rhcloud.com
Source0: fur
Source1: %{name}

Requires: python3 rpmdevtools mock

%description
Fedora User Repository CLI

Experimental version on command line client for Fedora User Repository

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}

cp -af %{SOURCE0} %{buildroot}%{_bindir}
cp -af %{SOURCE1} %{buildroot}%{_sysconfdir}

install -d %{buildroot}%{_bindir}

%files
%{_bindir}/fur
%{_sysconfdir}/%{name}

%changelog
* Tue Aug 23 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.6.0-1
- Release 0.6.0
- Fixes through the entire code
- Support for other architectures
- https instead of http to get spec file

* Mon Aug 22 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.5.1-1
- Turn off debug mode

* Mon Aug 22 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.5.0-1
- Release 0.5.0
- Drop .spec parsing code around getting Sources/Patches and just use Fedora spectool
- Use mockchain instead of mock to prepare for BuildRequires from FUR
- cleaning up

* Mon Aug 8 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.1.1-1
- Release 0.1.1
- Support for %{name} and %{version} in Sources and Patches

* Mon Aug 8 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.1.0-1
- Release 0.1.0
