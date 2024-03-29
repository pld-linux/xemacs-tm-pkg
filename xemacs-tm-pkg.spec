Summary:	[X]Emacs MIME support
Summary(pl.UTF-8):	Wsparcie do MIME dla [X]Emacsa
Name:		xemacs-tm-pkg
%define 	srcname	tm
Version:	1.39
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	dd747c6f21e7e28b7facb546b4fa231f
#Patch0:	xemacs-tm-pkg-info.patch
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-gnus-pkg
Requires:	xemacs-mh-e-pkg
Requires:	xemacs-rmail-pkg
Requires:	xemacs-vm-pkg
Requires:	xemacs-mailcrypt-pkg
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-apel-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
[X]Emacs MIME support.

%description -l pl.UTF-8
Wsparcie do MIME dla [X]Emacsa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/tm/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_datadir}/xemacs-packages/lib-src/*
