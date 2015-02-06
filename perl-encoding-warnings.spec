%define upstream_name	 encoding-warnings
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Warn on implicit encoding conversions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AU/AUDREYT/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch
Provides:	perl(encoding::warnings)

%description
This perl pragma emits warnings whenever an ASCII character string
containing high-bit bytes is implicitly converted into UTF-8. It
is useful when working with mixed encoding strings.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/encoding/*
%{_mandir}/*/*


%changelog
* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.1
+ Revision: 505339
- rebuild using %%perl_convert_version

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.11-1mdv2010.0
+ Revision: 372675
- adding explicit provides, lowercase provides not automatically extracted - sigh
- update to 0.11

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 241213
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-2mdv2008.0
+ Revision: 86356
- rebuild


* Mon Jul 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-1mdv2007.0
- New version

* Sun May 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.05-2mdk
- Rebuild

* Thu Jul 22 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.05-1mdk
- Initial MDK release.

