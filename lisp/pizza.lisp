(defvar *pizza_list* nil)
(defvar *single_pizza* nil)
(defvar *topping_list* nil)
(defvar *total_cost* nil)
(setf *total_cost* 0)
(defvar *topping_cost* nil)
(setf *topping_cost* 0)
(defvar *pcount* nil)
(setf *pcount* 0)

(defvar *valid_toppings* (list 1 2 3 4 5 6 7) )
(defvar *valid_toppings_string* (list "Bacon" "Olives" "Ham" "Mushrooms" "Pineapple" "Salami" "Anchovies" ) )
(defvar *ynarray* (list 1 2))
(defvar *pizzasizearray* (list 1 2 3))


(defun add_pizza_to_list (pizza_to_add)
	(push pizza_to_add *order-pizza-list*)
)

(defun add_toppings (toppint_to_add)
	(push toppint_to_add *order-pizza-list*)
)

; Function to print a prompt and read a line of input
(defun prompt-read (prompt)
	(format *query-io* "~a: " prompt)
	(read *query-io*)
)

(defun topping_name (n)
	(decf n)
       ;"Returns the Nth element of LIST.
     ;N counts from zero.  If LIST is not that long, nil is returned."
      (car (nthcdr n *valid_toppings_string*)))


(defun printList (list)
	(loop for item in list
		do (format t " ~s" (topping_name item))
	)
)

(defun get_toppings(list)

	(if (null list)
		(print "")
			(progn
				(setq top1 (car list))
				(print top1)
				(setq other_top (cdr list))
				(get_toppings other_top )
			)
	)
	)

(defun get_list_length (list)
  (if list
    (1+ (get_list_length (cdr list)))
    0))

(defun print_order(list)

	(if (null list)
		(print "")
			(progn
				(incf *pcount*)
				(format t "~C"  #\linefeed)
				(format t "Pizza ~s Detail:" *pcount*)
				(setq single_pizza (car list))
				;(print "Single pizza: ")
				;(print single_pizza)
				(setq toppings (car single_pizza))
				(print "Toppings:")
				;(print (get_list_length toppings))
				(setf top_price (get_list_length toppings))
				(setf *topping_cost* (+ top_price *topping_cost* ))
				;(print toppings)
				(printList toppings)

				(setq price_size (cdr single_pizza))
				(setq price (car price_size))
				(print "Price:")
				(format t " ~s" price)
				(setf *total_cost* (+ price *total_cost* ))
				;(print price)
				(setq size (cdr price_size))
				(print "Size:")
				;(print size)
				(format t " ~s" size)
				(setq newlist (cdr list))
				(print "--------------------------------------------------------------------------------------")
				(print_order newlist )
			)
	)
	)

(defun main()
	
	(setf *single_pizza* nil)
	(setf *topping_list* nil)

	(print "Select Pizza Size:  1 = Large ($12) | 2 = Medium ($8) | 3 = Small ($5)")

	(loop
		(print "Your choice: ") 
		(setq choice (read))
		(if (not (find choice *pizzasizearray* :test #'equalp))
			(format T "Invalid choice: Please Enter 1 or 2 or 3")
			(return)
			
		)
	)

	(if (= 1 choice)
		(progn
		(setf price  12)
		(push "Large" *single_pizza*)
		(push 12 *single_pizza*)
		)
	)

	(if (= 2 choice)
		(progn
		(setf price  8)
		(push "Medium" *single_pizza*)
		(push 8 *single_pizza*)
		)
	)

	(if (= 3 choice)
		(progn
		(setf price  5)
		(push "Small" *single_pizza*)
		(push 5 *single_pizza*)
		)
	)

	(defvar topping nil)
	(defvar topping_count nil)
	(setf topping_count 1)
	(print "Select Toppings:   1 = Bacon | 2 = Olives | 3 = Ham | 4 = Mushrooms | 5 = Pineapples | 6 = Salami | 7 = Anchovies") 
	;(print "Maximum four topping allowed.")
	(loop

		(print "Which topping do you like to add?")
			(setq topping (read))

			(if (not (find topping *valid_toppings* :test #'equalp))
				(format T "Invalid choice - please choose 1 to 7.~%")
				(progn
					;(format t "Topping count ~a.~%~%" topping_count)
					(if (not (null topping))
						(progn
							(incf topping_count)
							(push topping *topping_list*)
							)

						)
					;(format T "Topping selected  ~a.~%~%" topping)
					(if (> topping_count 4)
						(progn
							(print "You have selected four topping!! which is maximum value.")
							(return)
						)
						(progn
							(loop
								(print "Do you like to add more topping? 1 = Yes  | 2 = No")
								(setq ynvalue (read))
								(if (not (find ynvalue *ynarray* :test #'equalp))
									(format T "Invalid choice - please choose 1 or 2.~%")
									(return)
									
								)
							)
							(if (= ynvalue 2)
								(return) 
							)
						) 				                     
					)
				)
		)
	)


		;(print *topping_list*)
		(push *topping_list* *single_pizza*)
		;(print *single_pizza*)
		(push *single_pizza* *pizza_list*)
		;(print *pizza_list*)
)


(main)


(loop
	(print "Do you like to add more pizza? 1 = Yes  | 2 = No")
	(setq ynvalue (read))
	(if (not (find ynvalue *ynarray* :test #'equalp))
		(format T "Invalid choice - please choose 1 or 2.~%")
		(progn
			(if (= ynvalue 1)
				(main) 
				(return)
			)

			)
			
	)
)

(print "Enter Your Name: ")
(setq name (read))

(print "Enter Your Phone: ")
(setq phone (read))

(loop
	(print "Select Delivary type? 1 = Delivary  | 2 = Collected")
	(setq ynvalue (read))
	(if (not (find ynvalue *ynarray* :test #'equalp))
		(format T "Invalid choice - please choose 1 or 2.~%")
		(progn
			(if (= ynvalue 1)
				(progn
					(print "Enter Your Address: ")
					(setq address (read))
					(return)
					)
				(return)
			)

			)
			
	)
)

;(print "Final")
;(print *pizza_list*)
(format t "~C"  #\linefeed)
(format t "~C"  #\linefeed)
(print "Your Order Details:")
(format t "~C"  #\linefeed)
;(print "*********************************************************************************************")
(print "*********************************************************************************************")

(print_order *pizza_list* )


(print "Delivary type: ")
(if (= ynvalue 1)
	(format t " ~s" "Delivary")
	(format t " ~s" "Collected")
	)


(print "Name: ")
(format t " ~s" name)

(print "Phone:")
(format t " ~s" phone)

(if (= ynvalue 1)
	(progn
		(print "Address: ")
		(format t " ~s" address)

		)
	)

;(print "Topping price: ")
;(format t " ~s" *topping_cost*)
(setf *total_cost* (+ *topping_cost* *total_cost*))
;(print "Total Price: $")
;(format t " ~s" *total_cost*)
(format t "~C"  #\linefeed)
(format t "Total Price: $~s" *total_cost*)


(if (and (= ynvalue 1) (< *total_cost* 30)) 
	(progn
		(print "Here total price is less than $30. so $8 Delivary fee will be added.")
		(setf *total_cost* (+ 8 *total_cost*))
		)
	)
;(print "Total Cost: $")

(format t "~C"  #\linefeed)
(format t "Total Price: $~s" *total_cost*)


(format t "~C"  #\linefeed)
;(print "*********************************************************************************************")
(print "*********************************************************************************************")
(format t "~C"  #\linefeed)
(format t "~C"  #\linefeed)

