# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"

    config.vm.network :forwarded_port, guest: 8000, host: 8000

    # # Add to /etc/hosts: 33.33.33.24 dev.example.com
    # config.vm.network :hostonly, "33.33.33.24"

    #config.vm.provision :puppet do |puppet|
    #    puppet.manifests_path = "puppet/manifests"
    #    puppet.manifest_file  = "vagrant.pp"
    #end
end
