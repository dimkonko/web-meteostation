# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "hashicorp/precise32"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "512"]
  end

  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 80, host: 8625

  config.vm.synced_folder "public_html/", "/var/www"

  config.vm.provision :shell, path: "./etc/bootstrap.sh", privileged: true
end
