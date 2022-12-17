package com.yanszero;

import com.yanszero.animals.Cat;
import com.yanszero.animals.Dog;
import com.yanszero.base.Animal;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Animal[] animals = new Animal[]{new Cat("cat"),new Dog("dog")};

        for (Animal animal: animals) {
            System.out.println("this animal is :" + animal.getName());
            animal.talk();
        }
    }
}
