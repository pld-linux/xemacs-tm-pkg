### Comment
# This file is modified automatically by 'xemacs-adapter' script
# from PLD-project CVS repository: cvs.pld.org.pl, module SPECS
# For more details see comments in this script
### EndComment

Summary: 	Emacs MIME support.
Summary(pl):	Emacs MIME support.

Name:    	xemacs-tm-pkg
%define 	srcname	tm
Version: 	1.21
Release:	1

# TODO: some infos don't rebuild
# set NoInfo
%define		NoInfo True
#Patch0: 	xemacs-tm-pkg-info.patch

### Preamble
License:	GPL
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:      	http://www.xemacs.org
Source:   	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires: 	xemacs
Requires: 	xemacs-gnus-pkg
Requires: 	xemacs-mh-e-pkg
Requires: 	xemacs-rmail-pkg
Requires: 	xemacs-vm-pkg
Requires: 	xemacs-mailcrypt-pkg
Requires: 	xemacs-mail-lib-pkg
Requires: 	xemacs-apel-pkg
Requires: 	xemacs-base-pkg
### EndPreamble

%description


%description -l pl 


### Main
%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
gzip -9nf lisp/tm/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT
### EndMain

### PrePost
### EndPrePost

### Files
%files
%defattr(644,root,root,755)
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
%{_datadir}/xemacs-packages/lib-src/*
%doc lisp/tm/ChangeLog.gz 
### EndFiles
