%global reponame crash-gcore
Name:           crash-gcore-command
Version:        1.6.3
Release:        1
Summary:        Command of Gcore for Crash utility

License:        GPLv2
URL:            http://people.redhat.com/anderson/extensions/%{name}-%{version}.tar.gz
Source:         %{name}-%{version}.tar.gz

Buildroot:      %{_tmppath}/%{name}-root
BuildRequires:  zlib-devel lzo-devel snappy-devel crash-devel >= 5.1.5 gcc
Requires:       crash >= 5.1.5

%description
The crash-gcore-command packages contain an extension module for the crash utility
that adds a "gcore" command which can create a core dump file of a user-space task
that was running in a kernel dumpfile.

%prep
%autosetup -n %{reponame}-%{version} -p1

%build
%make_build -C src -f gcore.mk

%install
install -D %{_builddir}/%{reponame}-%{version}/src/gcore.so %{buildroot}%{_libdir}/crash/extensions/gcore.so

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/crash/extensions/gcore.so

%changelog
* Tue Jan 18 2022 SimpleUpdate Robot <tc@openeuler.org> - 1.6.3-1
- Upgrade to version 1.6.3

* Mon May 31 2021 baizhonggui <baizhonggui@huawei.com> - 1.3.1-2
- Add gcc in BuildRequires

* Thu Nov 28 2019 daiqianwen <daiqianwen@huawei.com> - 1.3.1-1
- Package init



