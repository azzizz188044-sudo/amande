document.addEventListener(
    "DOMContentLoaded",
    function () {

        const translations = {

            "Add":
                "Qo‘shish",

            "Add another":
                "Yana qo‘shish",

            "Change":
                "O‘zgartirish",

            "Delete":
                "O‘chirish",

            "Save":
                "Saqlash",

            "Save and continue editing":
                "Saqlash va davom etish",

            "Save and add another":
                "Saqlash va yana qo‘shish",

            "Save as new":
                "Yangi sifatida saqlash",

            "Cancel":
                "Bekor qilish",

            "Search":
                "Qidirish",

            "Filter":
                "Filtrlash",

            "Clear":
                "Tozalash",

            "Clear all filters":
                "Barcha filtrlarni tozalash",

            "Home":
                "Bosh sahifa",

            "View on site":
                "Saytda ko‘rish",

            "History":
                "Tarix",

            "Change history":
                "O‘zgarishlar tarixi",

            "Yes":
                "Ha",

            "No":
                "Yo‘q",

            "Select all":
                "Barchasini tanlash",

            "Select":
                "Tanlash",

            "Delete selected":
                "Tanlanganlarni o‘chirish",

            "Are you sure?":
                "Ishonchingiz komilmi?"

        };


        function translateText(
            element
        ) {

            if (
                element.children.length === 0
            ) {

                const text =
                    element.textContent.trim();


                if (
                    translations[text]
                ) {

                    element.textContent =
                        translations[text];

                }

            }

        }


        document
            .querySelectorAll(
                "body *"
            )
            .forEach(
                translateText
            );


        document
            .querySelectorAll(
                "input[type='submit'], button"
            )
            .forEach(
                function (element) {

                    const value =
                        element.value ||
                        element.textContent.trim();


                    if (
                        translations[value]
                    ) {

                        if (
                            element.value
                        ) {

                            element.value =
                                translations[value];

                        } else {

                            element.textContent =
                                translations[value];

                        }

                    }

                }
            );

    }

);