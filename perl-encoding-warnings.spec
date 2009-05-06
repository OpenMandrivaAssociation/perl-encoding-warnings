%define module	encoding-warnings
%define name	perl-%{module}
%define version	0.11
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Warn on implicit encoding conversions
License:	GPL or Artistic
Group:		Development/Perl
Source0:    http://search.cpan.org/CPAN/authors/id/A/AU/AUDREYT/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
Provides:   perl(encoding::warnings)

%description
This perl pragma emits warnings whenever an ASCII character string
containing high-bit bytes is implicitly converted into UTF-8. It
is useful when working with mixed encoding strings.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/encoding/*
%{_mandir}/*/*

