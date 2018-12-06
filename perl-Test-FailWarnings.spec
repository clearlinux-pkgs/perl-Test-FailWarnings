#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-FailWarnings
Version  : 0.008
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-FailWarnings-0.008.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-FailWarnings-0.008.tar.gz
Summary  : 'Add test failures if warnings are caught'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Test-FailWarnings-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)

%description
NAME
Test::FailWarnings - Add test failures if warnings are caught
VERSION
version 0.008

%package dev
Summary: dev components for the perl-Test-FailWarnings package.
Group: Development
Provides: perl-Test-FailWarnings-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-FailWarnings package.


%package license
Summary: license components for the perl-Test-FailWarnings package.
Group: Default

%description license
license components for the perl-Test-FailWarnings package.


%prep
%setup -q -n Test-FailWarnings-0.008

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-FailWarnings
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-FailWarnings/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Test/FailWarnings.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::FailWarnings.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-FailWarnings/LICENSE
