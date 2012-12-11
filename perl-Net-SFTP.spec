%define upstream_name	 Net-SFTP
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Secure File Transfer Protocol client
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DB/DBROBINS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Net::SSH::Perl)
BuildArch:	noarch

%description
This is Net::SFTP, a module implementing a client for the Secure
File Transfer Protocol.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Net
%{_mandir}/*/*


%changelog
* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 409038
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 241790
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.10-2mdv2008.0
+ Revision: 25201
- rebuild


* Mon Oct 10 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdk
- new version 
- %%mkrel
- rpmbuildupdate aware
- spec cleanup
- better summary
- fix directory ownership

* Wed Jan 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.09-1mdk
- 0.09

* Fri Feb 13 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.08-1mdk
- initial import, ltp requires it.

