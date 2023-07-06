#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Alien
%define		pnam	GMP
Summary:	Alien::GMP - provide the C gmp library
Name:		perl-Alien-GMP
Version:	1.16
Release:	4
License:	LGPL v3
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	961ac6e4c8a1cb53ad266134d6338a06
URL:		https://metacpan.org/release/Alien-GMP
BuildRequires:	gmp-devel
BuildRequires:	perl-Alien-Base
BuildRequires:	perl-Alien-Build >= 2.12
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
BuildRequires:	perl-FFI-CheckLib
BuildRequires:	perl-Test-Alien
BuildRequires:	perl-Test2-Suite >= 0.000060
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
This module provides gmp for other modules to use.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Alien/GMP.pm
%{perl_vendorarch}/Alien/GMP
%dir %{perl_vendorarch}/auto/Alien/GMP
%{perl_vendorarch}/auto/Alien/GMP/GMP.txt
%{perl_vendorarch}/auto/share/dist/Alien-GMP
%{_mandir}/man3/Alien::GMP.3pm*
