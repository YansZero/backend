package com.yanszero.animals;

import com.yanszero.base.Animal;

public class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public void eat() {
        System.out.println(super.getName() + " eat fish!");
    }

    @Override
    public void talk() {
        System.out.println(super.getName() + " is meow meow");
    }

    @Override
    public void mating(Animal animal) {
        System.out.println(super.getName() + "is mating with " + animal.getName());
    }
}
