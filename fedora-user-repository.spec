%define debug_package %{nil}

Name:    fedora-user-repository
Version: 0.1.1
Release: 1
Summary: Fedora User Repository
BuildArchitectures: noarch
License: GPLv2+
URL:     https://experimental-fur.rhcloud.com
Source0: fur
Source1: %{name}

Requires: python3

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
* Mon Aug 8 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.1.1-1
- Release 0.1.1
- Support for %{name} and %{version} in Sources and Patches

* Mon Aug 8 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.1.0-1
- Release 0.1.0
