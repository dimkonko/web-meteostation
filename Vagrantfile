# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "hashicorp/precise32"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "512"]
  end

  # guest(VM):host
  config.vm.network "forwarded_port", guest: 80, host: 80

  # config.vm.synced_folder "public_html/", "/var/www"
  config.vm.synced_folder ".", "/var/www"

  config.vm.provision :shell, path: "./etc/bootstrap.sh", privileged: true
end
